# Application Météo

Ce projet est une application météo qui affiche les prévisions météorologiques des 4 prochains jours comprenant la température moyenne, la température maximale, 
la température minimale, les précipitations et une description du code météo. Les données sont récupérées en utilisant des API météorologiques prises sur le site [https://open-meteo.com/en/docs/meteofrance-api](https://open-meteo.com/en/docs/meteofrance-api) et affichées dans un tableau HTML sur une page Quarto.

## Table des matières

- [Application Météo](#application-météo)
  - [Table des matières](#table-des-matières)
  - [Aperçu](#aperçu)
  - [Configuration](#configuration)
  - [Utilisation](#utilisation)


## Aperçu

L'application météo récupère les données météorologiques en temps réel à partir de différentes sources et les affiche dans un tableau HTML. Voici un aperçu des fonctionnalités clés de l'application :

- Affiche la température actuelle pour les 4 prochains jours.
- Affiche la température maximale et minimale pour chaque jour.
- Affiche les précipitations prévues pour chaque jour.
- Affiche une description du code météo pour chaque jour.

## Configuration

L'application utilise des API météorologiques pour récupérer les données. Voici les API utilisées et comment configurer l'application :

- API de température moyenne : L'application utilise l'API Open Meteo pour récupérer la température moyenne. Vous devrez remplacer les coordonnées de latitude et de longitude dans la fonction `fetchCurrentTemperature` avec les coordonnées de votre emplacement.

- API de température maximale, minimale et précipitations : L'application utilise l'API Open Meteo pour récupérer ces données. Assurez-vous également que les coordonnées de latitude et de longitude sont correctes dans la fonction `fetchMaxMinTemperatureAndPrecipitations`.

- API de code météo : L'application utilise l'API Open Meteo pour récupérer les codes météo. Vérifiez les coordonnées dans la fonction `fetchWeatherCode`.

- Ce code ajouté à mon script JavaScript fera en sorte que les données météorologiques soient récupérées et mises à jour automatiquement toutes les 15 minutes une fois que la page est chargée. 

```java
// Actualise les données toutes les 15 minutes (en millisecondes)
setInterval(function() {
    fetchCurrentTemperature();
    fetchMaxMinTemperatureAndPrecipitations();
    fetchWeatherCode();
}, 15 * 60 * 1000); // 15 minutes en millisecondes
```
## Utilisation

Pour utiliser cette application météo j'ai publié mon site web sur GithubPages, il suffit alors de cliquer sur l'URL du site suivant : 

romeobex.github.io/Application-_meteo-/
