# Testausdokumentti

Suorituskykytestejä varten loin projektini juureen tiedoston `performance_tests.py`, joka sisältää suorituskykytestin jokaiselle
matriisilaskutoimitukselle. Jokaista matriisilaskutoimitusta on testattu sata kertaa n*n matriiseilla, missä n=10,20,30,40,50
ja joissa solujen arvot ovat satunnaisgeneroitu kokonaislukuväliltä [-10,10].

Testit ovat helposti toistettavissa. Tämä hoituu suorittamalla projektini juuressa oleva tiedosto `performance_tests.py` esim.
komentoriviltä käsin komennolla `python3 /path/to/my/project/directory/performance_tests.py`. Kannattaa varautua odottamaan
tuloksia vähintään kaksikymmentä minuuttia. Jos kärsivällisyys on kuitenkin vaakalaudalla, voi tiedoston alussa olevaa
globaalia muuttujaa n pienentää sadasta esimerkiksi kymmeneen.

Alla on vielä pĺain text muodossa Kapsin lakka-palvelimella suoritettuna `performance_tests.py`:n antamat tulokset.
## Tulokset
```
ADDING TWO 10x10 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 12.243000000000059ms
average time: 0.1224300000000006ms

ADDING TWO 20x20 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 38.1490000000001ms
average time: 0.381490000000001ms

ADDING TWO 30x30 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 116.16700000000047ms
average time: 1.1616700000000046ms

ADDING TWO 40x40 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 175.2390000000008ms
average time: 1.752390000000008ms

ADDING TWO 50x50 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 293.38600000000457ms
average time: 2.933860000000046ms

CALCULATING THE DETERMINANT OF A 10x10 MATRIX WITH VALUES IN RANGE [-10, 10]
  total time: 277.55000000000194ms
average time: 2.7755000000000196ms

CALCULATING THE DETERMINANT OF A 20x20 MATRIX WITH VALUES IN RANGE [-10, 10]
  total time: 2502.7609999999986ms
average time: 25.027609999999985ms

CALCULATING THE DETERMINANT OF A 30x30 MATRIX WITH VALUES IN RANGE [-10, 10]
  total time: 9382.383999999996ms
average time: 93.82383999999996ms

CALCULATING THE DETERMINANT OF A 40x40 MATRIX WITH VALUES IN RANGE [-10, 10]
  total time: 36904.43999999999ms
average time: 369.0443999999999ms

CALCULATING THE DETERMINANT OF A 50x50 MATRIX WITH VALUES IN RANGE [-10, 10]
  total time: 91554.01600000006ms
average time: 915.5401600000006ms

INVERTING 10x10 MATRIX WITH VALUES IN RANGE [-10, 10]
  total time: 2133.372999999807ms
average time: 21.333729999998067ms

INVERTING 20x20 MATRIX WITH VALUES IN RANGE [-10, 10]
  total time: 18514.97899999981ms
average time: 185.1497899999981ms

INVERTING 30x30 MATRIX WITH VALUES IN RANGE [-10, 10]
  total time: 75676.10600000003ms
average time: 756.7610600000003ms

INVERTING 40x40 MATRIX WITH VALUES IN RANGE [-10, 10]
  total time: 246519.56199999986ms
average time: 2465.1956199999986ms

INVERTING 50x50 MATRIX WITH VALUES IN RANGE [-10, 10]
  total time: 647321.5820000011ms
average time: 6473.215820000011ms

MULTIPLYING TWO 10x10 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 136.5719999994326ms
average time: 1.365719999994326ms

MULTIPLYING TWO 20x20 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 1184.3730000000505ms
average time: 11.843730000000505ms

MULTIPLYING TWO 30x30 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 3921.94599999857ms
average time: 39.2194599999857ms

MULTIPLYING TWO 40x40 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 9240.744000000632ms
average time: 92.40744000000632ms

MULTIPLYING TWO 50x50 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 14413.544000000684ms
average time: 144.13544000000684ms

SUBSTRACTING TWO 10x10 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 14.106000000538188ms
average time: 0.14106000000538188ms

SUBSTRACTING TWO 20x20 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 46.2049999989631ms
average time: 0.46204999998963103ms

SUBSTRACTING TWO 30x30 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 104.09500000014305ms
average time: 1.0409500000014305ms

SUBSTRACTING TWO 40x40 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 188.2189999989805ms
average time: 1.882189999989805ms

SUBSTRACTING TWO 50x50 MATRICES WITH VALUES IN RANGE [-10, 10]
  total time: 310.1919999999154ms
average time: 3.1019199999991542ms
```
