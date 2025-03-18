
import requests

# Constants for the test
BASE_URL = "https://reqres.in/"  # Replace with your actual site URL
ADMIN_API = f"{BASE_URL}/api/users"  # Admin API endpoint for user creation
LOGIN_URL = f"{BASE_URL}/login"
HEADLESS = True

def create_user():
    """Create a user using the admin API and delete it after the test."""
    user_data={
        "name": "morpheus",
        "job": "leader",
        "id": "609",
        "createdAt": "2024-12-13T05:48:01.257Z"
    }

    # Create the user
    response = requests.post(ADMIN_API, json=user_data)
    assert response.status_code == 201, "User creation failed"
    user_id = response.json().get("name")
    print(response.status_code)
    print(user_id)
    user_data1={
        "name": "sarika",
        "job": "QA",
        "id": "609",
        "createdAt": "2024-12-13T05:48:01.257Z"
    }

    response=requests.post(ADMIN_API,json=user_data1)
    assert response.status_code==201
    print(response.status_code)
    user_name=response.json().get("name")
    print(user_name)

obj=create_user()
