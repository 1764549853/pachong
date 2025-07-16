import os
import requests

# 从环境变量中获取网址
url = os.environ.get("TARGET_URL")

# 从环境变量中获取用户名和密码，并组合成请求参数
params = {
    "username": os.environ.get("USERNAME"),
    "password": os.environ.get("PASSWORD"),
}

# 检查 url 是否存在，以避免 requests.post 收到 None
if url:
    # 发送 POST 请求
    response = requests.post(url=url, data=params)

    # 打印响应内容（假设响应是文本）
    print(response.content.decode())
else:
    print("错误：TARGET_URL 环境变量未设置。")
