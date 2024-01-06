import requests
from datetime import datetime

# De URL van het CRUD-eindpunt
crud_endpoint_url = "https://iot.pxl.bjth.xyz/api/v1/temperature"

# Huidige timestamp verkregen in float value int(timestamp) voor omzetting naar int
timestamp = int(datetime.now().timestamp())
#data that will be put in the database
payload = {
	"id": timestamp, #retrieves time in seconds from 1970-now
	"value": 0,	 #value is the temperature
	"scale": "C"	 #type of data in this case Celcius
}

#necessary info for the server
headers = {
    "Content-Type": "application/json",
    "X-Api-Key": ""#dont share this part!
}

#execute the crud "put" command 
response =requests.put(crud_endpoint_url,headers=headers,json=payload)

# Print the response of the server in cmd
print("Raw Response Content:", response.text)

