import requests

# Testing 'POST /user' operation documented in API

print("\n** Creating new Booking **\n")
url_post_booking = "http://127.0.0.1:8900/booking/"
headers = {'Content-type': 'application/json'}
data = {"date": "2019-10-27T18:25:43.511Z", "destination": "DUB",
        "id": "pepe@pepe.pe1-0.2", "origin": "MAD"}
response = requests.post(url_post_booking, json=data, headers=headers)
print(response)
print(response.content)
assert response.status_code == 201

# Get bookings:
print("\n** Displaying all Bookings after POST**\n")
url_get_booking = "http://127.0.0.1:8900/booking?id=pepe@pepe.pe1-0.2"
response = requests.get(url_get_booking)
print("Response: ", response)
print("Response content: ", response.content)

print("\n** Try deleting Bookings **\n")
response = requests.delete(url_get_booking)

print("Deleting bookings; response should be \"Method not allowed\":", response)
assert response.status_code == 405

