#The CRUD-endpoint URL
crud_endpoint_url = "iot.pxl.bjth.xyz/api/v1/temperature"

#Format to send
payload = {

 "id": <UNIX TIME>,

 "value": TEMP,

 "scale": "Celsius"
}

#Headers
headers = {
    "Content-Type": "application/json",
}

# Read data from files
with open('in_temp0_raw', 'r') as f:
    TEMP_RAW = int(f.read())

with open('in_temp0_scale', 'r') as f:
    TEMP_SCALE = float(f.read())

with open('in_temp0_offset', 'r') as f:
    TEMP_OFFSET = float(f.read())

#Calculate temperature
TEMP = ((TEMP_RAW - TEMP_OFSET) / TEMP_SCALE)

#Send POST request
requests.post(crud_endpoint_url, json=payload, headers=headers)

'''
#Debugging code
try:
    # Stuur een POST-verzoek naar het CRUD-eindpunt
    response = requests.post(crud_endpoint_url, json=payload, headers=headers)

    # Controleer of het verzoek succesvol was (status code 2xx)
    if response.status_code // 100 == 2:
        print("Succesvol verstuurd naar het CRUD-eindpunt.")
    else:
        print(f"Fout bij het versturen naar het CRUD-eindpunt. Status code: {response.status_code}")

except Exception as e:
    print(f"Fout bij het uitvoeren van het verzoek: {str(e)}")
'''