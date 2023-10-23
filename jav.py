import requests

# L'URL de l'API
api_url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&current=temperature_2m&hourly=temperature_2m,precipitation,windspeed_10m"

# Effectuer la requête GET
response = requests.get(api_url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Extraire les données
    hourly_data = data.get("hourly", {})

    if "temperature_2m" in hourly_data and isinstance(hourly_data["temperature_2m"], list):
        temperatures = hourly_data["temperature_2m"]
        print("Température (°C) heure par heure:")
        for temperature in temperatures:
            if isinstance(temperature, dict):
                print(f"{temperature['time']} : {temperature['value']}°C")

    if "precipitation" in hourly_data and isinstance(hourly_data["precipitation"], list):
        precipitation = hourly_data["precipitation"]
        print("\nQuantité de précipitation (mm) heure par heure:")
        for precip in precipitation:
            if isinstance(precip, dict):
                print(f"{precip['time']} : {precip['value']} mm")

    if "windspeed_10m" in hourly_data and isinstance(hourly_data["windspeed_10m"], list):
        windspeed = hourly_data["windspeed_10m"]
        print("\nForce du vent (m/s) heure par heure:")
        for wind in windspeed:
            if isinstance(wind, dict):
                print(f"{wind['time']} : {wind['value']} m/s")
else:
    print(f"La requête a échoué avec le code d'état {response.status_code}")

#Temperature h par h stockées dans temperatures type liste
#Quantité de précipitations h par h dans precipitation type liste
#Force du vent dans windspeed type liste