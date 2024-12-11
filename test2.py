#github版本 通过github secret掩盖密码
import os
import requests

url = "https://www.imslr.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LcUBc&inajax=1"

# 从环境变量中获取用户名和密码
params = {
    "username": os.environ.get("USERNAME"),
    "password": os.environ.get("PASSWORD"),
}

response = requests.post(url=url, data=params)
print(response.content.decode())
