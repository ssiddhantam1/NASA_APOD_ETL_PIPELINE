from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import sqlite3

def fetch_nasa_apod():
    url = "https://api.nasa.gov/planetary/apod?api_key=nJxi6EIet9UsTrbH50o54pESGvwlLVi8uwzcWvjr"
    response = requests.get(url)
    data = response.json()

    title = data["title"]
    explanation = data["explanation"]
    date = data["date"]
    hdurl = data.get("hdurl") or data.get("url")
    filename = title.replace(" ", "_") + ".jpg"

    # Download image
    image_response = requests.get(hdurl)
    with open(filename, "wb") as f:
        f.write(image_response.content)

    # Insert into SQLite
    conn = sqlite3.connect("/usr/local/airflow/include/nasa_apod.db")

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS apod (
            date TEXT PRIMARY KEY,
            title TEXT,
            explanation TEXT,
            image_path TEXT
        )
    """)
    cursor.execute("""
        INSERT OR IGNORE INTO apod (date, title, explanation, image_path)
        VALUES (?, ?, ?, ?)
    """, (date, title, explanation, filename))
    conn.commit()
    conn.close()

    print(f"Saved APOD for {date}: {title}")

# DAG definition
default_args = {
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    dag_id="nasa_apod_dag",
    schedule="@daily",
    default_args=default_args,
    catchup=False,
    description="Download and log NASA APOD data to SQLite",
) as dag:

    fetch_task = PythonOperator(
        task_id="fetch_apod_image",
        python_callable=fetch_nasa_apod
    )
