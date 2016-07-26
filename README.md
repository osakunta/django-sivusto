Django-sivusto
==============

Sisällysluettelo
----------------
- Vaatimukset
- Kehitysserverin käynnistys
- Front-endin muutokset
- TODO

Vaatimukset
-----------
- Python 3.5
- Pip3
- Virtualenv asennettuna

Kehitysserverin käynnistys
--------------------------
Luo Python 3.5 virtualenv haluamaasi hakemistoon (älä kuitenkaan repon sisälle).
Seuraava komento luo virtualenvin sen hetkiseen hakemistoon:
```
virtualenv -p /usr/bin/python3.5 [virtualenvin-nimi]
```

Varmista, että virtualenv on aktivoitu:
```
source [virtualenvin-nimi]/bin/activate
```

Asenna kaikki tarvittavat Python-paketit, jotka on listattuna tiedostossa
requirements.txt. Huomaa, että asentamiseen tarvitaan nimenomaan pip3:a.
```
pip3 install -r requirements.txt
```

Mikäli pakettien asennus ei onnistu, ja saat tällaisen ilmoituksen:
> Could not find function xmlCheckVersion in library libxml2. Is libxml2 installed?

Varmista, että seuraavassa komennossa olevat paketit on asennettu:
```
sudo apt-get install -y python-lxml libxml2-dev libxslt1-dev
```

Jos haluat päivittää paketteja, jotta ne ovat ajan tasalla requirements.txt:n
kanssa, lisää `-U`-switch.
```
pip3 install -U -r requirements.txt
```

Käynnistä serveri repon juuressa:
```
python manage.py runserver
```

---

Front-endin muutokset
---------------------
Vaatii node.js:n ja npm:n sekä muutaman paketin globaalisti asennettuna.
```
npm install -g bower
npm install -g grunt
```

Käytettävät frameworkit ovat hakemistossa `assets/`. Täällä
`bower_components/` sisältää kaikki asennetut frameworkit. Älä muokkaa kyseisen
hakemiston tiedostoja itse, sillä bower huolehtii niiden versionhallinnasta.

Omat tiedostot lisätään hakemistoon `input/` ja näihin voi tehdä muutoksia.
Grunt huolehtii tiedostojen parsimisesta Djangon käyttöön. Ennen muutosten
tekemistä käynnistä terminaalissa Gruntin watch-toiminto komennolla:
```
grunt
```
Nyt kun teet muutoksia input-hakemiston tiedostoihin, Grunt huomaa muutokset
automaattisesti ja esimerkiksi sass-tiedostoja muuttaessa parsii ne yhdeksi
css-tiedostoksi, joka kopioidaan Djangon staattisiin tiedostoihin hakemistosta
`output/`.

TODO
----

### Backend
- Automaattinen kirjautuminen
    - Autentikointi kuitenkin ensimmäistä kertaa adminpaneeliin mennessä

### Frontend
- Varmista footerin ja navigaation responsiivisuus
