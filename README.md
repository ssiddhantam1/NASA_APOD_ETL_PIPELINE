# 🚀 NASA APOD ETL Pipeline

This project automates the daily retrieval of NASA's Astronomy Picture of the Day (APOD) using the NASA Open API. It uses Apache Airflow to orchestrate the workflow, stores image metadata in a SQLite database, and is fully containerized with Docker.

---
## 📷 Workflow Diagram
![workflow](https://github.com/user-attachments/assets/5c0cf950-bb30-4f6f-8316-e6611e128e99)


## 🔧 Tech Stack

- **Apache Airflow** (via Astro CLI)
- **Docker** (5-container setup)
- **SQLite** (local persistent storage)
- **Python 3.11+**
- **NASA APOD API**

---

## 🔁 What It Does

- Connects daily to the NASA APOD API
- Downloads the high-res APOD image
- Stores:
  - `title`
  - `date`
  - `explanation`
  - `image filename`
- Inserts into a **SQLite database** (`nasa_apod.db`)
- Fully managed via **Airflow DAG**

---

## ⚙️ How to Run This Locally

### 1. Clone the Repo

```bash
git clone https://github.com/ssiddhantam1/NASA_APOD_ETL_PIPELINE.git
cd NASA_APOD_ETL_PIPELINE

## Start Airflow via Astro CLI
astro dev start
This launches 5 Docker containers for:

Scheduler

Webserver

Triggerer

DAG processor

Postgres (metadata)

🗃️ Database: nasa_apod.db
Located in include/

Viewable with DB Browser for SQLite

Table schema:
| Column        | Type | Description                  |
| ------------- | ---- | ---------------------------- |
| `date`        | TEXT | APOD publish date            |
| `title`       | TEXT | Title of the image           |
| `explanation` | TEXT | NASA's APOD description      |
| `image_path`  | TEXT | Filename of downloaded image |

📊 Visualization (Coming Soon)
A Dash-based dashboard to browse the APOD archive from the database is still under progress.

📄 License
MIT License

🙌 Credits
NASA APOD API

Apache Airflow

Astronomer CLI

Built with ❤️ to explore the stars programmatically.
