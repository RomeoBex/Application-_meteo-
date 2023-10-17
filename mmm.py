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
#%%
#Ici on va essayer de changer les jours de la semaine sur ma page web en foncion de l'heure 

#obtention du nom du jour de la semaine:
j1=datetime.date.today()
jour1_semaine = j1.strftime("%A")
j2 = date_actuelle + datetime.timedelta(days=1)
jour2_semaine= j2.strftime("%A")
j3 = date_actuelle + datetime.timedelta(days=2)  # Ajoute 2 jours pour obtenir le 3ème jour
jour3_semaine = j3.strftime("%A")
j4 = date_actuelle + datetime.timedelta(days=3)  # Ajoute 3 jours pour obtenir le 4ème jour
jour4_semaine = j4.strftime("%A")


# %%
