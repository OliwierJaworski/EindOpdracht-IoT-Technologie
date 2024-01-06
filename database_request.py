import requests
from datetime import datetime

# De URL van het CRUD-eindpunt
crud_endpoint_url = "https://iot.pxl.bjth.xyz/api/v1/temperature"

# Huidige timestamp verkregen in float value int(timestamp) voor omzetting naar int
timestamp = int(datetime.now().timestamp())


payload = {
	"id": timestamp
}

# Voorbeeld headers (pas dit aan aan je behoeften)
headers = {
    "Content-Type": "application/json",
    "X-Api-Key": "mmm"
}
response =requests.get(crud_endpoint_url,headers=headers)

# Print the response
print("Raw Response Content:", response.text)

# Probeer de respons als JSON te parsen
try:
    response_json = response.json()
    print("Parsed JSON Response:", response_json)
except Exception as e:
    print("Error parsing JSON:", str(e))