import pytest
from jsonschema import validate
import requests

BASE_URL="https://jsonplaceholder.typicode.com/posts"

def test_get_request():
    response=requests.get(BASE_URL)
    print(response.status_code)
    # print("...",response.json())
    print("..",response.json()[0]["id"])
    assert response.status_code==200
    # assert response.json()['id']=='1'

# @pytest.mark.parametrize("input ")
def test_post_request():
    schama = {
        "userId": 1,
        "title": "this is reference book ",
        "body": "this is book impt"
                "\nfor reading 1"
                "\n and listing 1 "
                "\n this is market1"
    },
    response=requests.post(f"{BASE_URL}",json=schama)
    print(response.status_code)
    assert response.status_code==201

def test_put_request():
    schama={"title": "this is reference book newly lanuch"}
    response=requests.put(BASE_URL,json=schama)
    print(response.status_code)
    assert response.status_code==200
    assert response.json()["title"]=="this is reference book newly lanuch"



