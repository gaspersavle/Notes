
05.01.2023
14:20
[[# Tags]]
[[# Reference]]

# Teme

## LookAhead
![[look_ahead.png]]
$$G_{i}= A_{i} \cdot B_{i}$$$$P_{i}= A_{i}\oplus B_{i}$$
$$ C_{out,i}= G_{i}+ P_{i} \cdot C_{out,i-1}$$

### Topologija
![[lookahead_topologija.png]]
- Zgornja meja za uporabo lookahead tehnologije so _4 biti_, saj kasneje postane pocasna zaradi:
	- _Velikega fanouta_, izhod carry out cuti kapacitivnosti vseh n kanalnih tranzistorjev pod njim ter kapacitivnost vseh p-kanalnih tranzistorjev, vezanih na carry in
	- _Velikega stevila zaporedno vezanih tranzistorjev_, kot vidimo v pullup in pulldown vezavi, kjer imamo 5 zaporedno vezanih tranzistorjev


## Logaritmicen LookAhead sestevalnik
![[logaritmicen_lookahead.png]]
- Po zaslugi vzporednega izvajanja operacij se na spodnjem primeru operacija izvede veliko hitreje
	- Spodnja izvedba ima 3 stopnje, napram 8 stopnjam zgornje izvedbe
- Enostavno izvedljivo za ANd in OR funkcije, za kompleksnejse jeizvedba zahtevnejsa zaradi obracanja faze
- Stevilo stopenj narasca z logaritmom stevila vhodov

### Primer - domino sestevalnik
![[domino_sestevalnik_primer.png]]
- Propagacija izvedena z OR funkcijo
- Generacija izvedena z AND funkcijo


## Mnozilniki
![[binarno_mnozenje.png]]
- Vsaka vrstica predstavlja zmnozek mnozenca z dolocenim bitom mnozitelja
	- Ce je trenutno opazovani bit v mnozitelju 1 prepisemo mnozenec
	- Ce je trenutno opazovani bit mnozitelja enak 0, kot parcialni produkt zapisemo same nicle
- Koncni rezultat je _bitni sestevek parcialnih produktov_


### Array mnozilnik
![[array_mnozilnik.png]]

- Vhod v vsako naslednjo stopnjo sta doticna parcialna zmnozka in _carry out prejsnje stopnje_

#### Kriticna pot
![[kriticna_pot_array_mult.png]]
- Idealni sestevalnik za to izvedbo je [[NDES predavanje 22.12.2022#Polni sestevalnik, izvedba s prenosnimi vrati | sestevalnik s prenosnimi vrati]], saj _ima minimalno zakasnitev racunanja carryja in sestevka_, saj je cas zmnozka odvisen tako od racunanja sestevka in carryja

### Mnozilnik s pomnjenjem Carryja
![[carry_pomnjenje.png]]
- Ta izvedba ima zakasnitev odvisno samo od zakasnitve carryja, zato lahko zacnemo uporabljati _klasicne sestevalnike_ 
![[floorplan.png]]

### Mnozilnik Wallace-Tree
![[wallace_tree.png]]
1. V 1. stopnji izracunamo parcialne produkte
2. v 2. stopnji premaknemo bite parcialnih produktov navzgor, da dobimo "invertirano piramido"
3. v 3. stopnji s 3 polnimi sestevalniki in enim polovicnim sestejemo preostanke parcialnih produktov v pravilno strukturo 2 bitov na stolpec
4. V zadnji stopnji nato s polovicnim sestavalnikom izvedemo koncni sestevek


- S spremembo vrstnega reda racunanja smo pospesili operacijo, saj smo v prvi stopnji paralelizirali sestevanje

![[koncna_struktura.png]]

![[zaporedje_operacij_wallace.png]]

### Povzetek
- Pri optimizaciji imamo razlicne cilje, kot pri binarnih sestevalnikih
- Pri vsakem primeru je treba identificirati kriticno pot za boljse poznavanje zakasnitve
- Mozne tehnike izvedbe:
	- Logaritemski mnozilniki (Wallaceovo Drevo)
	- Kodiranje podatkov
	- Cevljenje

## Bit-shifterji
![[binarni_shifter.png]]
- Dovoli 3 operacije od katerih je le ena lahko v stanju 1
	- Pomik levo
	- Pomik desno
	- Brez operacije (nop)
- Vecino povrsine integriranega vezja zasedajo _povezave_
![[povezave_shifter.png]]
- Stevilo kontrolnih bitov je enako stevilu pomikov, torej bi za 

### Logaritemski pomikalni register
![[log_shifter.png]]
- S 3 kontrolnimi biti imamo teoreticno _8 kombinacij_
|SH4|SH2|SH1|Premik za ... mest|
|----|----|--|--|
|0|0|0|0|
|0|0|1|1|
|0|1|0|2|
|0|1|1|3|
|1|0|0|4|
|1|0|1|5|
|1|1|0|6|
|1|1|1|7|
- Ce je SH1 na stanju " 1 ", se bit A3 preslika na A2 in tako naprej vse do A0, ker so vsi ostali SH biti na "0" so odprye linije za prenos vrednosti na izhod, torej na izhodu dobimo vhodno zaporedje bitov, _le za 1 mesto zamaknjeno_
-  Stevilo kontrolnih signalov je _logaritem stevila pomikov_     $N_{kontrolnih} = \log_{2} (N_{premikov})$
-  Z istim layoutom lahko dosezemo razlicno stevilo premikov















# Reference
# Tags
#ndes #adders #multipliers #bitShifters