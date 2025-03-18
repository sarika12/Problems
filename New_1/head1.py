import requests
BASE_URL = "https://reqres.in/api/users"


response=requests.head(BASE_URL)
print(response.status_code)
for key, value in response.headers.items():
    print(f"{key}: {value}")

