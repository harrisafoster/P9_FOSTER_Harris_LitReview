# P9_FOSTER_Harris
LitReview

Projet 9 OpenClassrooms

## Application web de revue de littérature qui permet à ses utilisateurs de :
- Créer une demande de critique
- Répondre à une demande de critique
- Créer et répondre à sa propre demande de critique
- S'abonner à d'autres utilisateurs
- Modifier toutes les options mentionnées ci-dessus

## Prérequis de base
- Une application de type 'terminal' - GitBash, Mintty, Cygwin (si vous êtes sur Windows) 
   ou les terminaux par défaut si vous utilisez Macintosh ou Linux. 
- Python 3.9

## Installation
### Pour les développeurs et utilisateurs (windows 10, mac, linux) :
#### Clonez la source de LitReview localement (en utilisant votre terminal) :
```sh
$ git clone https://github.com/harrisafoster/P9_FOSTER_Harris
$ cd P9_FOSTER_Harris
```
##### Dans votre terminal dans le dossier P9_FOSTER_Harris/ : Créer et activer un environnement virtuel avec (windows 10) :
```sh
$ python -m venv env
$ source ./env/Scripts/activate
```
##### Créer et activer un environnement virtuel avec (mac & linux) :
```sh
$ virtualenv venv
$ source venv/bin/activate
```
##### Et installez les packages requis avec :
```sh
$ pip install -r requirements.txt
```
## Utilisation
### Vous pouvez mettre l'application web LitReview en route depuis votre terminal avec :
```sh
$ cd P9LR
$ python manage.py runserver
Puis accédez à votre port 8000 sur votre navigateur sur http://127.0.0.1:8000/
```
### Vous pouvez créer un compte admin et accéder à l'espace admin avec :
```sh
$ cd P9LR
$ python manage.py createsuperuser
$ Username: admin
$ Email address: admin@example.com
$ Password: **********
$ Password (again): *********
$ Superuser created successfully.

Puis dans votre navigateur http://127.0.0.1:8000/admin/
```

## Mode d'emploi

Au moment de l'accès à votre serveur personnel de LitReview vous allez voir une page d'authentification et inscription.
Vous pouvez créer votre compte ainsi qu'accéder à votre compte depuis cette page. Une fois authentifié, vous aurez accès
à votre flux, flux personnel, abonnements, et les modifications de toutes ces options. Vous aurez aussi accès à une
fonctionnalité pour vous déconnecter. 


## Built with
Python 3.9 

Django 3.2