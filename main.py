import requests # Allows ypu to access the API

#Allows you to get a response and code to see if the request was successful
response = requests.get(url="http://api.open-notify.org/iss-now.json")

#You can use the following to test the response to see if it was successful. However, not very efficient.
# if response.status_code != 200:
#     raise Exception("Bad response from API")

# A more efficient use of request via response variable to print out what status code was passed back.
response.raise_for_status()

#Now to get the data
data = response.json()
print(data)

# To get a data of a particular key
data=response.json()
print(data)
#Get individual data
longitude = data["iss_position"]["longitude"]
print("Longitude: " + longitude)
latitude = data["iss_position"]["latitude"]
print("Latitude" + latitude)


