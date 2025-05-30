import requests
param={
    "page":1,
    "per_page":1
}
url = "https://gorest.co.in/public/v2/users/"
rsp = requests.get(url,params=param)
print(rsp.status_code)
print(rsp.json())
