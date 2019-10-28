# api-test

I have created various python files to test the REST operations defined for this API:

booking-controller:
----------------------------
GET /booking
test_FetchBooking.py

POST /booking
test_CreateNewBooking.py

user-controller:
----------------------------
GET /user
test_FetchUserData.py

POST /user
test_CreateNewUser.py

GET /user/all
test_FetchAllUserData.py


Development & Launch notes: 
----------------------------
The provided jar server file was launched via the windows cmd prompt using the provided command:  
java -Dserver.port=8900 -jar AppPerformanceTest-0.1-SNAPSHOT.jar

All development and debugging was performed using the Python IDE PyCharm. I chose Python as the development language since it is 
what I’m used to using recently (Bash/Python). 

The python files are standalone and can be run through PyCharm or any other similar IDE; 
or can be run alternatively on a Windows command prompt, or on a Linux command line. 

Due to time restrictions I was only able to create these individual files to test the listed API operations. 
Further improvements would be needed such as:
•	Covering more use cases.
•	Automating the tests. 
•	Performance testing. 
•	Security testing. 
