import requests
url="https://www.imslr.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LcUBc&inajax=1"
params={
    "username":"3179681062@qq.com",
    "password":"Aoterman2000"
}
response=requests.post(url=url,data=params)
print(response.content.decode())

