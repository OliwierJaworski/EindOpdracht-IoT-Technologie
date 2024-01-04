# The CRUD-endpoint URL
crud_endpoint_url = "iot.pxl.bjth.xyz/api/v1/temperature"

# ??
payload = {

 "id": <UNIX TIME>,

 "value": <FLOAT>,

 "scale": "<STRING>"

}

# Headers
headers = {
    "Content-Type": "application/json",
}

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