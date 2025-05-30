import requests
header={"accept":"text/plain",
        "Content-Type":"application/json" }

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/12",headers=header)
print(response.json())

put_payload = {
  "id": 111,
  "title": "Vikas Swami",
  "dueDate": "2025-05-27T18:11:41.666Z",
  "completed": True
}

header_put={"accept":"text/plain",
        "Content-Type":"application/json" }
response_put =requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/12",headers=header_put,json=put_payload)

print(response_put.status_code)
print(response_put.json())
rs = response_put.json()
print(rs["id"])