import numpy as np
import matplotlib.pyplot as plt
import datetime
import requests
import json
import io
import base64
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Obtenez la date actuelle
date_actuelle = datetime.datetime.now()
jour_actuel = date_actuelle.strftime("%A")

l = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
l2 = []

if jour_actuel == 'Monday':
    l2 = [l[0], l[1], l[2], l[3], l[4]]
elif jour_actuel == 'Tuesday':
    l2 = [l[1], l[2], l[3], l[4], l[5]]
elif jour_actuel == 'Wednesday':
    l2 = [l[2], l[3], l[4], l[5], l[6]]
elif jour_actuel == 'Thursday':
    l2 = [l[3], l[4], l[5], l[6], l[0]]
elif jour_actuel == 'Friday':
    l2 = [l[4], l[5], l[6], l[0], l[1]]
elif jour_actuel == 'Saturday':
    l2 = [l[5], l[6], l[0], l[1], l[2]]
else:
    l2 = [l[6], l[0], l[1], l[2], l[3]]

# Requête GET à l'URL de l'API météo
api_url = "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&hourly=temperature_2m,windspeed_10m,winddirection_10m&start_date=2023-09-24&end_date=2023-09-28"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    # Extrayez les données de température, force du vent et direction du vent
    temperatures = data.get('hourly', {}).get('temperature_2m', [])
    vent_force = data.get('hourly', {}).get('windspeed_10m', [])
    vent_direction = data.get('hourly', {}).get('winddirection_10m', [])

    # Calcul des températures moyennes par jour
    jours = len(temperatures) // 24  # Calcul du nombre de jours complets dans les données

    moyennes_temperatures = []

    for jour in range(jours):
        debut = jour * 24
        fin = (jour + 1) * 24
        moy_temp_jour = sum(temperatures[debut:fin]) / 24
        moyennes_temperatures.append(moy_temp_jour)

    # Calcul des températures maximales et minimales par jour
    temp_max = [max(temperatures[jour * 24:(jour + 1) * 24]) for jour in range(jours)]
    temp_min = [min(temperatures[jour * 24:(jour + 1) * 24]) for jour in range(jours)]

    # Créez un tableau
    fig, ax = plt.subplots(figsize=(12, 0.1))  # Définissez les dimensions de la figure ici
    table_data = []

    # Ajoutez la colonne "Caractéristique"
    caracteristique = ["Caractéristiques météo","Température Moyenne","Température Maximale","Température Minimale","Force du vent (km/h)","Direction du vent"]
    table_data.append(caracteristique)

    for day, moy_temp, temp_max_jour, temp_min_jour, force_vent, direction_vent in zip(
            l2, moyennes_temperatures, temp_max, temp_min, vent_force, vent_direction):
        moy_temp_formatted = f"{moy_temp:.1f}"  # Formatage de la moyenne avec un chiffre après la virgule
        temp_max_formatted = f"{temp_max_jour:.1f}"
        temp_min_formatted = f"{temp_min_jour:.1f}"
        force_vent_formatted = f"{force_vent:.1f}"
        direction_vent_formatted = f"{direction_vent:.1f}"

        # Obtenez l'icône du soleil en fonction de la température
        if moy_temp >= 25:
            sun_icon = ""
        elif moy_temp >= 20:
            sun_icon = "C:\Users\romeo\Documents\Infos\doc_python\soleil.soleil.png" 
        elif moy_temp >= 15:
            sun_icon = "s"
        else:
            sun_icon = "a"

        table_data.append(
            [day, f"{moy_temp_formatted} {sun_icon}", temp_max_formatted, temp_min_formatted, force_vent_formatted,
             direction_vent_formatted])
    
    # Transpose la liste pour avoir les jours en tant que colonnes
    table_data = list(map(list, zip(*table_data)))

    tableau = ax.table(cellText=table_data, cellLoc='center', loc='center',
                       cellColours=[['#f0f0f0'] * 6] * len(table_data))

    # Couleur de fond
    fig.patch.set_facecolor('#87CEEB')

    # Ajuster la mise en forme du tableau
    tableau.auto_set_font_size(False)
    tableau.set_fontsize(7.5)  # Taille de la police

    # Personnalisez la couleur du texte dans les cellules du tableau
    for i, key in enumerate(table_data):
        for j, value in enumerate(key):
            if i == 0:
                tableau[(i, j)].set_text_props(weight='bold', color='blue')  # Couleur du texte dans la ligne d'en-tête
            else:
                tableau[(i, j)].set_text_props(color='black')  # Couleur du texte dans les autres lignes

    # Masque les axes du graphique
    ax.axis('off')

    # Remplacez '/chemin/vers/votre/repertoire' par le chemin d'enregistrement souhaité
    chemin_d_enregistrement = 'C:/Users/romeo/Documents/Infos/doc_python/tableau_meteo.png'
    chemin_d_enregistrement2 = 'C:/Users/romeo/Documents/Infos/doc_python/tableau.html'

    # Enregistrez l'image au format PNG
    fig.savefig(chemin_d_enregistrement, bbox_inches='tight', dpi=300)  # Augmentez dpi pour une meilleure résolution

    # Convertissez l'image en base64
    with open(chemin_d_enregistrement, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()

    # Créez le contenu HTML en incorporant l'image base64
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tableau Meteo</title>
    </head>
    <body>
    <h1>Tableau Meteo</h1>
    <img src="data:image/png;base64, {base64_image}" alt="Tableau Meteo">
    </body>
    </html>
    ''' 

    # Enregistrez le contenu HTML dans le fichier HTML
    with open(chemin_d_enregistrement2, 'w') as html_file:
        html_file.write(html_content)

else:
    print("La requête à l'API a échoué.")