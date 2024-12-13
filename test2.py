
import os
import requests

url = os.environ.get("TARGET_URL")


params = {
    "username": os.environ.get("USERNAME"),
    "password": os.environ.get("PASSWORD"),
}

response = requests.post(url=url, data=params)
print(response.content.decode())
