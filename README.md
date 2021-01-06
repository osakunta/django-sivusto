Django-sivusto
==============

[![Build Status](https://travis-ci.org/osakunta/django-sivusto.svg?branch=master)](https://travis-ci.org/osakunta/django-sivusto)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cf01cdfce3604499b46cba91613fd123)](https://app.codacy.com/app/Osakunta/django-sivusto?utm_source=github.com&utm_medium=referral&utm_content=osakunta/django-sivusto&utm_campaign=Badge_Grade_Dashboard)

Vaatimukset
-----------
- Python 3.7
- Pip3
- Virtualenv asennettuna


Ennen kehitysserverin käynnistystä
----------------------------------

Kopioi kehitystietokanta
```
cp development.db.seed db.sqlite3
```

Kehitysserverin käynnistys
--------------------------

### Virtualenv

Luo Python 3.7 virtualenv
```
virtualenv -p /usr/bin/python3.7 venv
```

Varmista, että virtualenv on aktivoitu:
```
source venv/bin/activate
```

### Riippuvuudet

Projektissa käytetään riippuvuuksien hallintaan `pipenv`iä. Riippuvuudet saa
asennettua seuraavasti:
```
pip install pipenv
pipenv install -d
```

Mikäli pakettien asennus ei onnistu, ja saat tällaisen tai vastaavan ilmoituksen:
> Could not find function xmlCheckVersion in library libxml2. Is libxml2 installed?

Varmista, että seuraavassa komennossa olevat paketit on asennettu:
```
sudo apt-get install -y python-lxml libxml2-dev libxslt1-dev libffi-dev libpq-dev
```


#### Ilmo-applikaatio
Repositorio sisältää [django-ilmo-app](https://github.com/osakunta/django-ilmo-app) Django-applikaation, joka on osana repositoriota submodulena.

Submodule on checkoutattu johonkin tietyyn committiin. Kun submodulesta halutaan käyttää HEAD committia sivuston tuotantoympäristössä, ajetaan komennot:
```
cd ilmo_app
git fetch
```

Otetaan `production`-branchista tuorein version:
```
git checkout production
git pull
```

Kun eri committiin on viitattu, lisätään muuttunut submodulen committi haluttuun branchiin:
```
cd ..
git add ilmo_app
git commit -m "Bump ilmo app"
```

Tuoreimman `production`-commitin käyttö voidaan automatisoida yo. komennoilla, kun CI-serverillä autentikoitu git-käyttäjä/-botti suorittaa komennot ja pushaa tuotantohaaraan.

### Käynnistys

Käynnistä palvelu repon juuressa:
```
python manage.py runserver
```

---

## Assets

Assets are built with Webpack. They are built from `assets/` directory to `sato/static/`. To install and build for dev environment, run

    npm install
    npm start
