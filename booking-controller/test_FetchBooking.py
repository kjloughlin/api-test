import requests

# Testing 'GET /booking' operation documented in API
print("\n** Displaying Bookings for given ID **\n")

# Assuming we know the ID of the user for whom we are looking for bookings
url_get_booking = "http://127.0.0.1:8900/booking?id=pepe@pepe.pe1-0.2"
response = requests.get(url_get_booking)

print("Response: ", response)
print("Response content: ", response.content)
