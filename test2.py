<<<<<<< HEAD
import os
import requests

# 从环境变量中获取网址
url = os.environ.get("TARGET_URL")

# 从环境变量中获取用户名和密码
=======

import os
import requests

url = os.environ.get("TARGET_URL")

params = {
    "username": os.environ.get("USERNAME"),
    "password": os.environ.get("PASSWORD"),
}

response = requests.post(url=url, data=params)
print(response.content.decode())
