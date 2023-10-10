import requests

# URL de l'API
url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&current=temperature_2m&hourly=temperature_2m,precipitation&daily=temperature_2m_max,temperature_2m_min&timezone=auto"

# Effectuer la requête HTTP
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Extraire les données
    temperature_current = data["current"]["temperature_2m"]
    temperature_max = data["daily"]["temperature_2m_max"]
    temperature_min = data["daily"]["temperature_2m_min"]
    
    # Données horaires de température et précipitations
    hourly_temperature = data["hourly"]["temperature_2m"]
    hourly_precipitation = data["hourly"]["precipitation"]
    
    # Stocker les données dans des variables
    temperature_actuelle = f"Température actuelle : {temperature_current}°C"
    temperature_maximale = f"Température maximale : {temperature_max}°C"
    temperature_minimale = f"Température minimale : {temperature_min}°C"
    
    temperature_heure_par_heure = []
    for hour, temp in enumerate(hourly_temperature):
        temperature_heure_par_heure.append(f"Heure {hour}:00 - Température : {temp}°C")
    
    precipitation_heure_par_heure = []
    for hour, precip in enumerate(hourly_precipitation):
        precipitation_heure_par_heure.append(f"Heure {hour}:00 - Précipitations : {precip} mm")
else:
    print("La requête a échoué. Code d'erreur :", response.status_code)

# Maintenant, vous pouvez accéder aux données dans les variables
print(temperature_actuelle)
print(temperature_maximale)
print(temperature_minimale)

print("Température heure par heure :")
for temp in temperature_heure_par_heure:
    print(temp)

print("Précipitations heure par heure (mm) :")
for precip in precipitation_heure_par_heure:
    print(precip)

