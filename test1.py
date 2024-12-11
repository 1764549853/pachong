import requests
url="https://www.imslr.com/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash=LcUBc&inajax=1"
params={
    "username":"1764549853@qq.com",
    "password":"Wertikeo1"
}
response=requests.post(url=url,data=params)
print(response.content.decode())