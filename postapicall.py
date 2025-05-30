import json
import requests

header={"accept":"text/plain",
        "Content-Type":"application/json" }

payload = {
  "id": 112,
  "title": "Test_string",
  "dueDate": "2025-05-28T18:10:38.666Z",
  "completed": True
}

jdata = open("json_data.py","r").read()
response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities",headers=header,json=payload)
print(response.status_code)
print(response.json())
j_response = response.json()
print(j_response["id"]==122) # True / False
assert j_response["id"]==112 ,"ID does not match"
assert response.status_code ==200 ,"status done does not match"