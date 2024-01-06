import requests
from datetime import datetime

# De URL van het CRUD-eindpunt
crud_endpoint_url = "https://crudcrud.com/api/ea7b147f27c649f8a5463b43eccb3d24/data"

# Huidige timestamp verkrijgen
timestamp = datetime.now().timestamp()

# Voorbeeld payload voor een POST-verzoek (pas dit aan aan je behoeften)
payload = {
    "time": timestamp  # Hier de timestamp toevoegen in plaats van "timestamp"
}

# Voorbeeld headers (pas dit aan aan je behoeften)
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
