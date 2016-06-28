Django-sivusto
==============

Vaatimukset
-----------
- Python 3.5
- Virtualenv asennettuna

Kehitysserverin käynnistys
--------------------------
Varmista, että virtualenv on aktivoitu (repon juuressa):
```
source env/bin/activate
```
Käynnistä serveri hakemistossa `project/`:
```
python manage.py runserver
```

---

Front-endin muutokset
---------------------
Vaatii node.js:n sekä npm:n ja versionhallintaa varten bowerin globaalisti
asennettuna (`npm install -g bower`).

Käytettävät frameworkit ovat hakemistossa `project/assets/`. Täällä
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
