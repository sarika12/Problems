import requests

url = "https://jsonplaceholder.typicode.com/posts"

data={
    "userId": 1,
    "id": 1,
    "title": "this is reference book ",
    "body": "this is book impt"
            "\nfor reading "
            "\n and listing "
            "\n this is market"
  },

response=requests.post(url=url,json=data)
print(response.status_code)
print(response.json())
assert response.status_code==201


data_udate={
    "userId": 1,
    "id": 1,
    "title": "this is reference book newly launch",

  },
response1=requests.put(f"{url}/1",json=data_udate)
print(response1.status_code)
print(response1.json())