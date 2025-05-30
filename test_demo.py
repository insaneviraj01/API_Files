import pytest
import requests


def test_get_req():
    head = {"Content-Type": "application/json",
            "x-api-key": "reqres-free-v1"
            }
    base_url ="https://reqres.in/api/users/2"

    respo = requests.get(url=base_url,headers=head)
    assert 200 == respo.status_code
    print(respo.text)