## Ohjelman rakenteesta
Ohjelmani toiminta rakentuu käytännössä yksinomaan hakemistossa `src/`sijaitsevista tiedoista
- `__init__.py`
- `calculator.py`
- `main.py`
- `Matrix.py`
- `my_algorithms.py`
- `parser.py`.

### __init__.py
Tyhjä `__init__.py` pitää olemassaolollaan huolen siitä, että hakemisto `src/` tulkitaan pakettihakemistoksi. Ilman tätä
tiedostoa, moduulit eivät voisi käyttää toisiaan. Esim. `calculator.py` ei voisi tuoda `Matrix.py`:ssä määriteltyä
Matrix-luokkkaa.

### calculator.py
Laskinoperaatiot ovat jokainen toteutettuna `calculator.py`-tiedostossa. Tämä tekee `calculator.py`:stä kurssin tavoitteiden
kannalta projektini tärkeimmän tiedoston. Tiedoston sisällä on siis toteutettuna kaksi minulle entuudestaan tuntematonta
algoritmia, jotka laskevat matriisin determinantin ja käänteismatriisin.

### main.py
Tämä tiedosto toimii käyttöliittymän wrapperina. Tiedostossa kutsutaan `parser.py`-tiedoston metodeja, jossa käyttäjältä
kysytään ja luetaan syötettä, joiden perusteella `main.py` kutsuu `calculator.py`:n metodeja.

### Matrix.py
Matriisi-luokka on toteutettuna `Matrix.py`-tiedoston sisällä. Luokka sisältää tärkeimmät tiedot matriisista, kuten sen koon,
rivit, ja skalaarin.

### my_algorithms.py
Omat versioni Pythonin valmisalgorimeista on toteutettuna `my_algorithms.py` tiedoston sisällä. Näitä tarvitaan esimerkiksi
`calculator.py` ja `parser.py` tiedostoissa. Omia tietorakenteita projektini ei vaadi, joten en ole toteuttanut mitään
Pythonin valmiita tietorakenteita itse.

### parser.py
Käyttöliittymän osat, joissa käyttäjältä halutaan lukea syötettä, on toteutettu tiedostossa `parser.py`. Tiedostossa on mm.
metodi, jossa luodaan matriisi-olio käyttäjän syötteen perusteella.
