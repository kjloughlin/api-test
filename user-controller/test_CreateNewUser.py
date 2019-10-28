import requests
import json
import jsonpath

# Testing 'POST /user' operation documented in API

# API URLs
url_post_user = "http://127.0.0.1:8900/user"

# Make POST request with Json Input body
headers_post = {'Content-type': 'application/json'}
json_data = {"email": "kieran@kieran", "name": "kieran", "id": "kieran@kieran.pe1-0.2", "bookings": []}
response = requests.post(url_post_user, json=json_data, headers=headers_post)
print("Posting new user; response should be 201 (Created)", response)
print("Response content: ", response.content)
assert response.status_code == 201

# Parse response to Json format. This is because the response we get from the POST call
# is in the string format. If we want to use it, we must parse to Json format
response_json = json.loads(response.text)
print("response_json:", response_json)

# Get ID using Json path
id_element = jsonpath.jsonpath(response_json, 'id')
print("Generated ID of new user:", id_element[0])

# Check that this new user actually appears in the database:
id_data = id_element[0]
user_url = "http://127.0.0.1:8900/user?id=%s" % id_data
response = requests.get(user_url)
assert response.status_code == 200
print("Response is: ", response.status_code)
print("Response content: ", response.content)

# HTTP method delete not listed in API - let's test that it returns 405:
id_data = id_element
delete_user_url = "http://127.0.0.1:8900/user?id=%s" % id_data
response = requests.delete(delete_user_url)

print("Deleting user; response should be \"Method not allowed\":", response)
assert response.status_code == 405
