import pytest
import requests
import json

# # Open and read the JSON file
# with open('data.json', 'r') as file:
#     data = json.load(file)
#
# # Print the data
#
#
# # Access specific elements
# if 'author' in data:
#     print(data["author"])



class TestAPI:


    url = "https://jsonplaceholder.typicode.com/posts/1"
        # Perform a GET request


    # API endpoint

    def test_get_call(self):


        response = requests.get(self.url)
        # Validate the response
        print("Status Code:", response.status_code)
        print("Response Body:", response.json())

        # Assertions (Test conditions)
        assert response.status_code == 200, "Failed: Status code is not 200"
        assert response.json()['id'] == 1, "Failed: ID does not match"
