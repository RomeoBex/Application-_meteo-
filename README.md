<html lang="en">  
<head>
    <meta charset="UTF-8">
    <!-- Ajoutez la balise meta viewport ici -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <title>Votre Titre</title>
    <!-- Inclusion des fichiers CSS externes -->
    <link rel="stylesheet" type="text/css" href="background.css">
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            background-image: url('sky-blue.jpg');
            background-size: cover;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            overflow-x: hidden; /* Empêche le défilement horizontal */
        }

        header {
            text-align: center;
            background-color: #60b0df;
            color: #fff;
            padding: 40px 0;
        }

        header h1 {
            font-size: 2em;
        }

        main {
            text-align: center;
            padding: 20px;
        }

        iframe {
            width: 100%;
            height: 800px; /* Hauteur définie à 500 pixels pour votre tableau */
            border: none; /* Supprime la bordure de l'iframe */
        }

        footer {
            position: relative; /* Change la position en relative pour que le pied de page suive le flux du contenu */
            margin-top: 25px;
            background-color: #66b3e0;
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <header> 
        <p> Voici les prévisions météorologiques des 5 prochains jours à Montpellier 
        </p>
    </header>

    <main>
        <iframe src="tableau.html" frameborder="0"></iframe>
    </main>

    <footer>
        <p>&copy; 2023 Roméo BEX <br>Données météorologiques : open-meteo.com </p>
    </footer>
</body>
</html> 
