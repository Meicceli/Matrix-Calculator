# Toinen viikkoraportti

## Testausviikko

### Keskiviikko 04.08. ja Torstai 05.08.
Nämä päivät sisälsivät todennäköisyyslaskentaa, [C:tä](http://mooc.fi/courses/2016/aalto-c/) ja lamaa (Laskennan mallit).


### Perjantai 05.08.
Tämä viikko on projektin kannalta koostunut yksinomaan testaamisesta. Perjantaina käytin runsaasti aikaa ensin selvittäen miten
koodia on järkevintä testata Pythonilla. Kävi ilmi, että testaaminen on Pythonissa hyvin samankaltaista, kuin mitä se on Javassa
(Junit).

Kun perustuntuma Pythonilla testaamiseen oli saatu, aloin kunnolla luomaan erilaisia testejä toteuttamilleni
matriisilaskutoimituksille. Tämä oli yllättävänkin aikaa vievää, ja erityisesti kertolaskun testaus 10x10 matriiseille oli
todella inhaa (oikean tuloksen laskin symbolisella laskimella).

Aikaa koodaamiseen kului noin viisi tuntia yhteensä.


### Lauantai 06.08. ja Sunnuntai 07.08.
Viikonlopun aikana työtunteja ei tullut yhteensä kuin ehkä kahden tunnin edestä. Kuitenkin testejä tuli runsain mitoin.
Perjantaina olin saanut jo valmiiksi laskimen toimintaa tarkastelevat testit, joten näille päiville jäi Matrix-luokan metodien
testaaminen. Loin siis testit, jotka testaava mm. sitä, että Matrix-olio luodaan oikein, ja että metodit getRow, getCol toimivat
oikein. Nämä testit oli huomattavasti nopeampi ja helpompi luoda kuin testit laskutoimituksille.

### Ongelmakohtia
Testaamisessa on joitain ongelmallisia kohtia, jotka tulisi selvittää:
- Miten testata järkevästi laskutoimitusten oikeellisuutta isoilla syötteillä?
- Miten voin testata interaktiivisia metodeja (ts. metodeja, jotka kysyvät käyttäjältä syötettä) ?

### Yhteenveto viikosta
Testaaminen Pythonilla tuli tutuksi, ja sain luotua kattavat (pieni)testit. Tähän olen tyytyväinen, mutta viikko jäi kuitenkin
tavoitteistani vajaaksi kun aliarvioin muiden kurssien vaatiman ajan, ja työnmäärää. Erityisesti laman yleistenttiin
valmistautuminen on syönyt suuren osan ajastani kuluneella viikolla.

Tarkoitus oli viikolla toteuttaa myös matriisin determinantin laskeva metodi, mutta tämä siirtyy ensi viikolle. Kuitenkin,
koska kattavat testit valmistuivat viikon aikana, ja koska olen aina koodia väkertäessäni myös kommentoinut koodiani, en ole
jäljessä [kurssin virallisesta aikataulusta](https://github.com/TiraLabra/2016-loppukesa/wiki/Aikataulu).

### Mitä ensiviikolla?
Aikaani valtavasti syönyt yleistentti on ohi tiistain jälkeen, jolloin minulle jää huomattavasti enemmän aikaa edistää
projektiani. Tavoitteenani on:
- saada ydin täysin valmiiksi (tämä tarkoittaa determinantin laskevan metodin toteuttamista)
- selvittää järkevä tapa testata laskutoimituksia suurilla syötteillä
- jos ajan puute ei pääse jälleen yllättämään, niin aloitan valmismetodien korvaamisen omillani
- miettiä ja ehkä jopa jo toteuttaa mahdollisia muita laskutoimituksia (käänteismatriisi kenties?)
