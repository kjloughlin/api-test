import requests
import json

# Testing 'GET /user' operation documented in API

# Construct query API URL
id_data = "pepe@pepe.pe1-0.2"
user_url = "http://127.0.0.1:8900/user?id=%s" % id_data

print("\n** Displaying specific users **\n")
response = requests.get(user_url)
assert response.status_code == 200

print("Response headers: ", response.headers)
print("Response content: ", response.content)

# Parse the response to Json format
json_response = json.loads(response.text)
print("JSON response for users...", json_response)
