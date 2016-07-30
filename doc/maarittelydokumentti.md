# Määrittelydokumentti

## Aihe
Tässä projektissa toteutan yksinkertaisen matriisilaskimen. Tarkoitus on toteuttaa seuraavat ominaisuudet
- Matriisien yhteen- ja vähennyslasku
- Matriisien kertolasku
- Matriisin determinantin määrääminen.
- Skalaarilla kertominen

## Toiminta
Ohjelmaa suoritatessa, käyttäjältä kysytään ensin matriisi rivi kerrallaan, ja tälle matriisille suoritettava operaatio.
Valitun operaation ollessa unaarinen (esim. kun valittu operaatio on determinantin määrääminen), suoritetaan annetulle
matriisille tämä operaatio välittömästi. Binääristen operaattoreiden kanssa käyttäjältä kysytään toinen matriisi, ja jos se on
yhteensopiva ensimmäisen matriisin kanssa (tämä riippuu operaattorista), niin ohjelman laskema tulosmatriisi tulostetaan
käyttäjälle.

## Tietorakenteet
Matriisilaskin ei vaadi monimutkaisia tietorakenteita. Matriisit voidaan tallentaa kaksiulotteiseen taulukkoon, jolloin
matriiseille suoritettavat operaatiot ovat helppoja, ja mahdollisimman tehokkaita. Olisi myös mahdollista tallentaa matriisit
merkkijonoina, kun merkitään esimerkiksi välilyönneillä sarakkeen vaihtoa, ja pystyviivalla rivin vaihtoa. Tämä kuitenkin
vaikeuttaisi (ja erityisesti, hidastaa) operaatioiden toimintaa merkittävästi.

## Algoritmit
Matriisin yhteen-, vähennyslaskun ja skalaarikertolaskun suorittamiselle ei tunneta nopeampaa tapaa kuin perinteiset
lineaarialgebran kursseilta tutut mekaaniset laskentatavat. Nämä toteutukset tulevat siis olemaan osa matriisilaskintani.

Kertolaskun toteutus tulee myös olemaan naiivi, vaikka aikavaativuudeltaan tehokkaampiakin algoritmeja
[löytyy](https://en.wikipedia.org/wiki/Strassen_algorithm#Asymptotic_complexity). Niissä on kuitenkin heikkouksena suurempi
muistin syönti ja huomattavasti vaativampi toteutus naiiviin algoritmiin verrattuna. Lisäksi aikavaativuus viittaamassani
Strassenin algoritmissa on noin luokkaa O(n^2.84), mikä on liian pieni parannus naiivin algoritmin O(n^3) aikavaativuuteen
ollakseen mielestäni sen jopa nelinkertaisen määrän alkioita vaatiman tilan arvoinen.

Determinantin laskeminen lienee koko projektin haasteellisin osuus. Tämän toteuttanen käyttäen n.k.
(LU-hajotelmaa)[https://en.wikipedia.org/wiki/LU_decomposition] jolloin determinantin laskemisen aikavaativuus on luokkaa
O(n^3).

## Tavoiteltavat aika- ja tilavaativuudet
Tavoitteeni tilavaativuudelle on O(k\*n\*m), missä k on jokin positiivinen kokonaisluku, n on korkeimman syötetyn matriisin
rivimäärä ja m leveimmän matriisin sarakkeiden lukumäärä. Tämä on realistinen tavoite, sillä mainitsemani algoritmit operoivat
korkeintaan n*m kokoisilla matriiseilla.

Yhteen-, ja vähennyslaskujen aikavaativuudet tulevat molemmat olemaan luokkaa O(n*m) (tämä lienee selvää). Kertolasku C = A*B
toteutuu naiivilla algoritmilla ajassa O(n\*m\*p), missä A on n*m matriisi, B m*p matriisi ja C n*p matriisi. Jos A ja B ovat
neliömatriiseja, tulee aikavaativuudeksi O(n^3).
