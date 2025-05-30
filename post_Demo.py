import requests

base_url ="https://reqres.in/api/users"

head = {"Content-Type":"application/json",
        "x-api-key": "reqres-free-v1"
        }

payloads = {
    "name": "Vikas",
    "job": "QA"}

respo = requests.post(url=base_url,headers=head,json=payloads)
print(respo.status_code)
print(respo.json())
