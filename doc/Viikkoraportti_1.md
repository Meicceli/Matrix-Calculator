# Ensimmäinen viikkoraportti

## Lauantai 30.7.
Aloin paiskimaan hommia noin. kello 16:30. Kirjoitushetkellä kello on noin 21:30, ja työtä on tehty taukoamatta. Tämä useamman
tunnin työurakka on kuitenkin ollut tuottoisaa.

Päätin aloittaa projektini koodaamalla ohjelman syötteenlukijan. Syötteenlukijasta oli helppo lähteä liikkeelle, sillä muu
tulee rakentumaan tämän päälle. Parser.py sisältää nimittäin myös ohjelman toiminnan kannalta elintärkeän Matrix-luokan.

Parser.py sisältää Matrix-luokan lisäksi pari apumetodia, joiden tarkoituksena on toimia käyttöliittymänä. Ne pyytävät käyttäjää
syöttämään matriisin/matriisit ja näille tehtävät operaatiot. Käyttäjän antamien matriisien perusteella luodaan Matrix-luokan
olioita, jotka palautetaan myöhemmin toteutettavalle wrapperille.

Parser.py sisältää myös dokumentaation sen toiminnasta. Ennen tätä projektia en ymmärtänytkään, kuinka helppoa dokumentoiminen
Pythonilla lopulta on. Yhden rivin kommentti metodin alle, ja se näkyy heti metodin kuvauksena tekstieditorini autocompletessa!
Opin myös, että tarkemmat kuvaukset metodeista voidaan antaa Pythonin tyyliohjeiden mukaisesti asettamalla yksi tyhjä rivi
ensimmäisen metodin nimen alla olevan kommenttirivin alle, jonka jälkeen seuraavalle riville voidaan alkaa kirjoittamaan
yksityiskohtaista kuvausta.

Määrittelydokumentti tuli myös valmiiksi tämän vuorokauden puolella. Sitä tehdessä tuli verestettyä Githubin käyttämän
markdownin perusteita.

Lyhyesti sanottuna, tänään olen saanut ohjelman syötteenlukijan valmiiksi määrittelydokumentin ohella, oppinut hieman lisää
Pythonin luokista, Pythonin tyylisuosituksista, sekä dokumentoinnista. Aikaa tähän kaikkeen kului noin viisi tuntia.


## Sunnuntai 31.7.
Päivän aikana valmiiksi tulivat yksinkertaiset matriisien laskutoimitukset, sekä yksinkertainen main tiedosto, jonka
suorittamalla voi laskea yhden laskutoimituksen per suorituskerta.

Varsinaisesti uusia asioita ei näitä toteuttaessa tullut vastaan. Toteutukset olivat hyvin suoraviivaisia.

Päivänaikana työtunteja kertyi noin nelisen tuntia.

## Mitä seuraavaksi?
Seuraavan viikon tavoitteena on saada aikaan uupuva matriisin determinantin laskeva moduuli. Tämä tulee luultavasti olemaan
seuraavan viikon haastavin toteutettava. Tämän lisäksi tarkoitus olisi saada kurssin tavoiteaikataulun mukaisesti valmiiksi
kattavat yksikkötestaukset. 

Lisäksi, jos jää aikaa muilta kursseilta, niin pyrin toteuttamaan jo omia versioita Pythonin valmisalgoritmeista. Työ ei
varsinaisesti sisällä mitään erityisempiä tietorakenteita (vaativin tietorakenne on 2D-taulukko), joita minun tarvisi itse
toteuttaa.

Lyhyesti sanottuna siis olen jo melko pitkällä projektissani. Kurssin toisen viikon aikataulun tavoitteista puuttuu oikeastaan
vain yksikkötestaaminen. Saatan olla ensi viikon maanantaihin mennessä saanut valmiiksi kolmannen viikon tavoitteet.
