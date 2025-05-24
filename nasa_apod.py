import json
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=nJxi6EIet9UsTrbH50o54pESGvwlLVi8uwzcWvjr"
response = requests.get(url)
print(response)

data = response.json()

title = data["title"]
explanation = data["explanation"]
print(f"The title is: {title} \n")
print(f"The explanation is: {explanation}")

hdurl = data.get("hdurl")

image_response = requests.get(hdurl)
filename = title.replace(" ","_") + ".jpg"
with open(filename, "wb") as f:
    f.write(image_response.content)

