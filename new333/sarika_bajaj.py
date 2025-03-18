import requests

#https://reqres.in/
header={"accept": "text/plain",
	   "Content-Type": "application/json"}
data={
    "name": "morpheus",
    "job": "leader"
}

response1=requests.get("https://reqres.in/api/users",headers=header,json=data)

assert response1.status_code =="200"
playlaod={
    "name": "sarika",
    "job": "leader"
}

response2=requests.post("https://reqres.in/api/users",json=data)
assert response2.status_code=="204"

