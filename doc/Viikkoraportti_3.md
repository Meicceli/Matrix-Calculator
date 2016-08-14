# 3. Viikkoraportti

## Torstai 11.08.
Ydin alkaa olemaan valmis! Sain nimittäin tänään torstaina toteutettua työn vaativimmat algoritmit, eli determinanttilaskimen,
sekä - alkuperäisestä suunnitelmasta poiketen - myös käänteismatriisilaskimen. Päivän aikana perehdyin lineaarialgebraan,
ottaen selvää LU-dekompositiosta ja sen toteuttamisesta. Ymmärtäessäni LU-dekomposition idean, sain melko nopeasti toteutettua
tämän koodini osaksi.

LU-dekomposition laskemisen jälkeen on hyvin helppoa laskea matriisin determinantti. LU-dekompositiossa neliömatriisi A nimittäin
hajoitetaan kahdeksi kolmiomatriisiksi L ja U, joiden determinantit saadaan helposti laskemalla diagonaalilla (vas. ylänurkka ->
oik. alanurkka) olevien lukujen tulo. Nyt, koska A=L*U, niin A:n determinantti saadaan laskealla det(L) * det(U).

LU-dekompositio on myös hyvin hyödyllinen matriisin käänteismatriisia etsittäessä, sillä kolmiomatriisien L ja U käänteismatriisit
ovat helppoja löytää. Nyt, koska A=L*U, voimme etsiä ratkaista matriisit L^-1 ja U^-1, jolloin A:n käänteismatriisi on
matriisi U^-1 * L^-1.

Päivän aikana sain myös luotua useampia testejä determinanttilaskimelle, ja korjasin myös `parser.py` tiedostossa Matrix-olion
getRowArray() metodin. Lisäksi tarkoitus olisi saada aikaan myös testit käänteismatriisin laskevalle metodille vielä tämän viikon
aikana.

## Lauantai 13.08.
Päivän aikana kehitin determinanttilaskinta, sekä käänteismatriisilaskinta. Lopetin kokonaan liukulukujen käsittelyn tarkkuuden
parantamiseksi. Liukulukujen sijasta käsittelen pareja (n, d), joka ajaa murtoluvun asemaa (n osoittaja, d jakaja). Python
pystyy laskemaan mielivaltaisen suurilla kokonaislukuja automaagisesti, joten tällainen murtolukukikkailu takaa täydellisen
tarkkuuden laskutoimituksia tehdessä.

Kuitenkaan tämä lähestymistapa ei ole kenties paras mahdollinen. Murtolukujen osoittajista ja nimittäjistä kasvaa nopeasti
todella suuria (suurempia kuin 10^100) käänteismatriisia laskettaessa, mikä tietysti hidastaa huomattavasti käänteismatriisin
etsimisprosessia. Lisäksi, kun luvut kasvavat noin suuriksi, niin Python ei pysty enää suorittamaan lopullista likiarvon
laskemista (n/d) kun käänteismatriisia tulostettaisiin käyttäjälle. Noh, ainakin determinantin laskeminen toimii nopeasti ja
tarkasti.

Viikon suurin ongelmakohta on siis käänteismatriisilaskimen testaus ja toteutus. Jos en käytä toteuttamaani
murtolukutaktiikkaa, käänteismatriisilaskin tuottaa pahasti virheellisiä tuloksia. Toisaalta, jos käytän murtolukutaktiikkaa,
koodistani tulee nopeasti käyttökelvotonta.

Ensi viikon tavoitteina olisi saada toteutus- ja testausdokumentaatiota aluilleen, sekä toteuttaa suurin osa käyttämistäni
valmisalgoritmeista itse. Testeihinkin voisi lisätä muutamia suorituskykyä testaavia metodeita.
