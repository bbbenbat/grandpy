# GrandPY


[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)

Ce projet concerne un site internet permettant de parler à un papy robot afin 
de lui demander une adresse. 

Il vous le donnera (via l'API GoogleMaps)
avec, en bonus, une histoire sur ce lieu (via l'API Wikipedia).

## Pour commencer

Vous devez posséder un compte Heroku afin de déposer le dossier via ce site.

L'application utilisant l'API de Google Maps avec deux clés privées, il vous faudra les créer sur le site 
officiel de Google https://console.cloud.google.com.


### Pré-requis

Avant tout chose, vous devez:

- avoir un compte Heroku (https://www.heroku.com).
- deux clés API GoogleMaps (https://console.cloud.google.com). 
- avoir installé Git sur son ordinateur (https://git-scm.com/downloads).
- avoir installé Python sur son ordinateur (https://www.python.org/downloads/).
- avoir installé le logiciel Heroku (https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
- télécharger le dossier "grandpy"

Vérifier que le dossier "grandpy" contient :
- app 
    * __init__.py
    * routes.py
    * controllers 
        * __init__.py
        * parser.py
    * models 
        * __init__.py
        * fr.json
        * google_api.py
        * wikipedia_api.py
    * static 
        * css
            * index.css
        * img
            * banc.jpg
            * papy.jpg
            * smile.jpg
        * js
            * form.js
    * templates
        * index.html
- test
    * __init__.py
    * test_google_api.py
    * test_parser.py
    * test_wikipedia_api.py
- README.md
- config.py
- Procfile
- requirements.txt

### Installation

#### Clé API Google
Une fois que vous avez créé les deux clés, il faudra appliquer une restriction HTTP sur une clé. Insérer en valeur 
l'url de votre application Heroku (voir section Heroku).

#### Préparation dossier
Faites une copie du repository sur votre ordinateur : git clone https://github.com/bbbenbat/grandpy.git.
Créer un fichier .env à la racine du dossier.
Ouvrer le fichier, puis enregistrer la clé n'ayant pas de restriction, sous la clé 'GOOGLE_API_KEY_B'.
Enregistrer la deuxième clé, ayant la restriction, sous la clé 'GOOGLE_API_KEY'.
```
GOOGLE_API_KEY = 'cle_avec_restriction'
GOOGLE_API_KEY_B = 'cle_sans_restriction'
```

#### Heroku
Ouvrer la console et entrer.
```
$ heroku login
```
aller sur le dossier telechargé.
```
$ cd grandpy
```
Créer l'application sur le site Heroku
```
$ heroku create
```
L'url du site créé s'affiche, la copier et l'enregister dans la restriction HTTP de la clé Google.
```
remote:        Done: 57.1M
remote: -----> Launching...
remote:        Released v5
remote:        https://serene-caverns-82714.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
```
Faire un commit sur le git local.
```
git commit -m "Demo"
```
Publier votre dossier sur heroku.
```
git push heroku main
```
Aller sur la console web du site Heroku et saisir les variables d'environnements 
contenu dans le fichier .env, dans l'onglet 'setting' section 'Config Vars'.

Le site est maintenant fonctionnel!

## Démarrage

Aller sur l'adresse de votre site.
Vous arrivez sur la page principale.
Poser votre question à GrandPy, il se fera un plaisir de vous répondre. 


## Fabriqué avec

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Serveur web local
* [Bootstrap](https://getbootstrap.com/) - Framework CSS (front-end)
* [GoogleMaps API](https://console.cloud.google.com/) - API Google Maps
* [Wikipedia API](https://wikipedia.readthedocs.io/en/latest/) - API Wikipedia

## Contributing

Si vous souhaitez contribuer, cliquer sur [CONTRIBUTING.md](https://github.com/bbbenbat/grandpy) pour soumettre votre pull request.

## Versions

**Dernière version stable :** 1.0


## Auteurs

* **Ben Bessayah** _alias_ [@bbbenbat](https://github.com/bbbenbat)


