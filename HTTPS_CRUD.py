import requests
import sys
import os
from datetime import datetime

if __name__ == "__main__":
    # Check if there are command-line arguments
    if len(sys.argv) > 1:
        api_thing = sys.argv[1]
        print(f"Received argument: {api_thing}")
    else:
        print("No argument provided.")
        
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
    "X-Api-Key": api_thing #dont share this part!
}

#execute the crud "put" command 
response =requests.put(crud_endpoint_url,headers=headers,json=payload)

# Print the response of the server in cmd
print("Raw Response Content:", response.text)


