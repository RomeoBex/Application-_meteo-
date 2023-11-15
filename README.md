# Application Météo

## Table des matières
- [Aperçu](#aperçu)
- [Configuration](#configuration)
- [Utilisation](#utilisation) 

## Aperçu
L'application météo est un projet simple affichant les prévisions météorologiques des 4 prochains jours, incluant la température moyenne, maximale, minimale, les précipitations et une description du code météo. Les données sont récupérées à partir de l'API météorologique de MeteoFrance ([Documentation API MeteoFrance](https://open-meteo.com/en/docs/meteofrance-api)) et présentées dans un tableau HTML sur une page Quarto.

### Fonctionnalités clés
- Affiche la température actuelle pour les 4 prochains jours.
- Affiche la température maximale et minimale pour chaque jour.
- Présente les précipitations prévues pour chaque jour.
- Affiche une description du code météo pour chaque jour.
- Affiche les données du vent

## Configuration
L'application utilise différentes API météorologiques pour récupérer les données. Voici comment configurer l'application :

### API de température actuelle
L'application utilise l'API Open Meteo pour récupérer la température actuelle. Remplacez les coordonnées de latitude et de longitude dans la fonction `fetchCurrentTemperature` avec celles de votre emplacement.

### API de température maximale, minimale et précipitations
L'application utilise l'API Open Meteo pour ces données. Assurez-vous que les coordonnées de latitude et de longitude sont correctes dans la fonction `fetchMaxMinTemperatureAndPrecipitations`.

### API de code météo
L'application utilise l'API Open Meteo pour récupérer les codes météo. Vérifiez les coordonnées dans la fonction `fetchWeatherCode`.

Le code JavaScript ci-dessous permet la mise à jour automatique des données toutes les 15 minutes une fois que la page est chargée.

```javascript
// Actualise les données toutes les 15 minutes (en millisecondes)
setInterval(function() {
    fetchCurrentTemperature();
    fetchMaxMinTemperatureAndPrecipitations();
    fetchWeatherCode();
}, 15 * 60 * 1000); // 15 minutes en millisecondes
```
## Site web 

Voici le lien du site : <https://romeobex.github.io/Application-_meteo-/>
