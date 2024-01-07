import requests
import sys
import os
from datetime import datetime   

if __name__ == "__main__":
    # Check if there are command-line arguments
    if len(sys.argv) > 1:
        api_thing = sys.argv[1]
        print("Received argument is used for the Crud action")
    else:
        print("No argument provided.")
        
# De URL van het CRUD-eindpunt
crud_endpoint_url = "https://iot.pxl.bjth.xyz/api/v1/temperature"

with open('/sys/bus/iio/devices/iio:device0/in_temp0_raw', 'r') as f:
    TEMP_RAW = int(f.read())
with open('/sys/bus/iio/devices/iio:device0/in_temp0_scale', 'r') as f:
    TEMP_SCALE = float(f.read())
with open('/sys/bus/iio/devices/iio:device0/in_temp0_offset', 'r') as f:
    TEMP_OFFSET = float(f.read())
#Calculate temperature
TEMP = ((TEMP_RAW - TEMP_OFFSET) / TEMP_SCALE)
print("temp : %d" % TEMP)
# Huidige timestamp verkregen in float value int(timestamp) voor omzetting naar int
timestamp = int(datetime.now().timestamp())
#data that will be put in the database
payload = {
	"id": timestamp, #retrieves time in seconds from 1970-now
	"value": TEMP,	 #value is the temperature
	"scale": "C"	 #type of data in this case Celcius
}

#necessary info for the server
headers = {
    "Content-Type": "application/json",
    "X-Api-Key": api_thing #dont share this pls 
}

#execute the crud "put" command 
response =requests.put(crud_endpoint_url,headers=headers,json=payload)

# Print the response of the server in cmd
print("Raw Response Content:", response.text)


