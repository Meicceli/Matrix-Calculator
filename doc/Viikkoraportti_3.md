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
