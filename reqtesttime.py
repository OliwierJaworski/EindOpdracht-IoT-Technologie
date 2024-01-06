from datetime import datetime
import requests

# Huidige datum en tijd
now = datetime.now()
print('Datum en tijd:', now)

# Unix-tijd omzetten
timestamp = datetime.timestamp(now)
print("Unix-tijd:", timestamp)

# Het CRUD-eindpunt URL
crud_endpoint_url = "https://iot.pxl.bjth.xyz/api/v1/temperature"

# Payload voor het POST-verzoek
payload = {
    "id": timestamp,  # Gebruik de Unix-tijd als id
    "value": 25.5,     # Voorbeeldwaarde voor de temperatuur (vervang dit met de gewenste waarde)
    "scale": "Celsius" # Vervang dit met de gewenste schaal (bijv. Celsius, Fahrenheit)
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
