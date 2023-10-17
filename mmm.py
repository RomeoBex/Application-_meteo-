import numpy as np 
import datetime
import requests 


# Coordonnées de la localisation (on a pris Montpellier)
latitude = 43.6109
longitude = 3.8763

# URL de l'API
url = f"https://api.open-meteo.com/v1/meteofrance?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"

# Effectuer la requête GET
response = requests.get(url)

# Vérifier si la requête a réussi (code 200)
if response.status_code == 200:
    data = response.json()

    # Récupérer les données de température horaire
    hourly_temperature = data.get('hourly', {}).get('temperature_2m', [])

else:
    print(f"Erreur lors de la requête. Code de réponse : {response.status_code}")

#A la fin de ce code on obtient une liste comptenant toutes la température h par h des 4jours de la semaine
print(hourly_temperature)

temp_actu_J1=
