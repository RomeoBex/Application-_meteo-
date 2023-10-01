<html lang="en">
<head>
    <meta charset="UTF-8">
    <!-- Ajoutez la balise meta viewport ici -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <title>Application Météo</title>
    <!-- Inclusion des fichiers CSS externes -->
    <link rel="stylesheet" type="text/css" href="background.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- En-tête de la page -->
    <header> 
        <p> Voici les prévisions météorologiques des 5 prochains jours à Montpellier 
        </p>
    </header>

    <!-- Contenu principal de la page -->
    <main>
        <h2>Tableau Météo</h2>
        <!-- Inclusion d'une iframe sans barre de défilement horizontal --> 
        <iframe src="tableau.html" width="90%" height="auto" frameborder="0"></iframe>
        <!-- Vous pouvez ajuster la largeur, la hauteur et d'autres styles ici -->
    </main>

    <!-- Pied de page de la page -->
    <footer>
        <p>&copy; 2023 Roméo BEX</p>
    </footer>
</body>
</html>
