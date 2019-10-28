import requests
import json

# Testing 'GET /user/all' operation documented in API

# API URL
user_url = "http://127.0.0.1:8900/user/all"

# First discovery test: test GET call documented in API works:

print("\n** Displaying all users **\n")
response = requests.get(user_url)
assert response.status_code == 200

print("Response headers: ", response.headers)
print("Response content: ", response.content)

# Parse the response to Json format
json_response = json.loads(response.text)
print("JSON response for users...", json_response)
