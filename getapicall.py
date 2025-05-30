import requests
head = {
    'Accept':'text/plain'
}
response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/1",headers=head)
print("Status Code :- ",response.status_code)
print("Json_Body")
print(response.json())
json_response = response.json()
print("Title :- ",json_response["title"])
print("ID :- ",json_response["id"])
assert response.status_code == 200


