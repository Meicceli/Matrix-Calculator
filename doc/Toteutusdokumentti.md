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


## Aika- ja tilavaativuudet
Käsittelen erikseen aika- ja tilavaativuudet `calculator.py`-tiedostossa toteutetuille matriisilaskutoimituksille.

### Matriisien yhteenlasku (matrixAddition)
Aikavaativuus on selvästi O(n²). Metodissa vaativin operaatio on itse yhteenlasku, joka muodostuu kahdesta sisäisestä
for-silmukasta, joista ensimmäinen for riippuu matriisein rivien määrästä, ja toinen (sisempi) for matriisien sarakkeiden
lukumäärästä antaen aikavaativuudeksi O(rivit*sarakkeet). Tämä sievee muotoon O(n²) neliömatriisien tapauksessa.

Muistia metodissa käytetään luonnollisesti O(n²) verran, sillä (neliö)matriisit tarvitsevat tämän verran tilaa.

### Matriisien vähennyslasku (matrixSubstraction)
Aika- ja tilavaativuudet ovat täysin samat kuin yhteenlaskussa. Metodissa käytetään hyödyksi tietoa A-B = A+(-1*B). Tällöin
vähennyslasku voidaan toteuttaa kertomalla B:tä skalaarilla -1 (O(1)), ja kutsumalla sitten yhteenlaskumetodia.

### Skalaarikertolasku (matrixScalarMultiplication)
Aika- ja tilavaativuus O(1). Skalaarillakertominen on hoidettu Matrix-luokan sisällä siten, että matriisioliolla on sisäisen
scalar muuttuja, jossa pidetään yllä skalaarikertoimen arvoa (oletusarvoisesti 1). Tämän muuttaminen on yksinkertainen
kertolasku self.scalar *= x.

### Matriisien kertolasku (matrixMultiplication)
Tilavaativuus on jälleen yksinkertaisesti O(n²). Metodissa on vakiomäärä matriiseja, jotka kukin vievät O(n²) tilaa.
Aikavaativuus taasen on nyt O(n³). Matriisikertolasku on toteutettu naiivisti, lineaarialgebran kursseilta tutulla tavalla.
Aikavaativuuden kannalta nopeammat toteutukset eivät ole kovin merkittävällä tavalla nopeampia, ja syövät muistia huomattavasti
enemmän. O(n³) aikavaativuuden voi havaita kolmesta sisäkkäisestä for-silmukasta, joissa jokainen riippuu matriisien kooista.
Neliömatriisien tapauksessa aikavaativuus sievenee muotoon O(n³).

### Matriisin determinantin laskeminen (matrixDeterminant)
TODO

### Käänteismatriisin laskeminen (matrixInversion)
TODO

## Parannettavaa
Projekti on mielestäni varsin onnistunut, eikä varsinaisia puutteita juuri ole. Työni pahin aukko on murtolukujen (ja
liukulukujen) tuen puute käyttäjän syöttämissä matriiseissa. Tämän paikkaaminen on kuitenkin varsin tehtävissä, ja ajattelin
korjata asian ennen loppupalautusta 5.9. Lisäksi matriisikertolaskua voisi kenties viritellä. Tälle on olemassa ajassa
O(n^2.807) toimiva algoritmi, joskin nopeusero tavalliseen naiiviin tapaan laskea matriisikertolasku tulee esille vasta kun
n>100.

## Lähteet
- [Matrix multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication)
- [Matrix multiplication algorithm](https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm)
- [LU decomposition](https://en.wikipedia.org/wiki/LU_decomposition)
- [LUP decomposition](http://rosettacode.org/wiki/LU_decomposition)
- [Determinant](https://en.wikipedia.org/wiki/Determinant)
- [Forward (and backward) substitution](https://en.wikipedia.org/wiki/Triangular_matrix#Forward_and_back_substitution)
