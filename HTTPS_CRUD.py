#The CRUD-endpoint URL
#crud_endpoint_url = "iot.pxl.bjth.xyz/api/v1/temperature"
crud_endpoint_url = "https://crudcrud.com/api/9a217728b59047d4bad1e8a87494eb36"

#Current time and date
now = datetime.now()

# Unix-tijd conversion
timestamp = datetime.timestamp(now)

#Format to send
payload = {

 "id": timestamp,

 "value": TEMP,

 "scale": "Celsius"
}

#Headers
headers = {
    "Content-Type": "application/json",
}

# Read data from files
with open('/sys/bus/iio/devices/iio:device0/in_temp0_raw', 'r') as f:
    TEMP_RAW = int(f.read())

with open('in_temp0_scale', 'r') as f:
    TEMP_SCALE = float(f.read())

with open('in_temp0_offset', 'r') as f:
    TEMP_OFFSET = float(f.read())

#Calculate temperature
TEMP = ((TEMP_RAW - TEMP_OFSET) / TEMP_SCALE)

#Debugging code
try:
    #Send POST request
    response = requests.post(crud_endpoint_url, json=payload, headers=headers)

    # Controleer of het verzoek succesvol was (status code 2xx)
    if response.status_code // 100 == 2:
        print("Succesvol verstuurd naar het CRUD-eindpunt.")
    else:
        print(f"Fout bij het versturen naar het CRUD-eindpunt. Status code: {response.status_code}")

except Exception as e:
    print(f"Fout bij het uitvoeren van het verzoek: {str(e)}")