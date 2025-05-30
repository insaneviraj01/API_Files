import requests
header={
    "Content-Type":"application/json",
    "Authorization":"Bearer cafccccd47a0d0ceb536887a3b9403f6563bf9d9fef26fc78fb6198e225c4606"}

body = {
    "id": 791588402,
    "name": "Dalian_Mic",
    "email": "Dalian_Mic@paucek.test498",
    "gender": "male",
    "status": "inactive"
  }
url = "https://gorest.co.in/public/v2/users"
respo = requests.post("https://gorest.co.in/public/v2/users",headers=header,json=body)
print(respo.status_code)
print(respo.json())
assert respo.status_code == 201 ,"error code, code does not match"
get_repo = requests.get(url+'/'+str(respo.json()['id']), headers=header)
print(get_repo.status_code)
print(get_repo.json())