Django-sivusto
==============

Vaatimukset
-----------
- Python 3.5
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
