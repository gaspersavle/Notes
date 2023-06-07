
22.12.2022
14:22
[[# Tags]]
[[# Reference]]

# Teme

## Genericni digitalni proicesor
![[digitalni_procesotr.png]]
### Gradniki
- Aritmeticna enota
	- bitno zrezano podatkovno vodilo
- Spomin
- Krmilna logika
- Povezave
### Dizajn po rezinah
![[dizajn_rezine.png]]
- za vsak bit obstajajo enake rezine


## Sestevalniki
- __Polni sestevalnik:__
![[polni_sestevalnik.png]]
- Osredotocimo se pretezno na status carry out bita, saj se z njim pogojuje zakasnitev vecbitnih sestevalnikov
	- _Carry status DELETE_ pomeni, da bo stestevalnik imel carry izhod na 0, ceprav ga bo na vhodu dobil
	- _Carry status GENERATE_ pomeni, da bo sestevalnik postavil carry out na 1, ceprav ga na vhodu ne bo nujno dobil
	- _Carry status PROPAGATE_ pomeni, da se bo carry in preslikal na carry out, to se dogaja ko sta A in B _razlicna_
- SUM izhod opravlja 3 vhodno _XOR_ funkcijo med vhodi, torej bo 1 _ko bo na vhodu liho stevilo enic_
	- To se lahko zgodi v 4 kombinacijah vhdodnih bitov
![[demorgan_sumator.png]]
-  Izhoda C in SUM izrazimo kot funkcijo _Carry statusov_ 
	- _Generate(G)_ = $A \cdot B$
	- _Propagate(P)_ = $A \oplus B$
	- _Delete(D)_ = $\bar{A}\cdot\bar{B}$
![[nove_spremenljivke_sestevalnik.png]]
- Prva linija zgornje funkcije je napacna, saj $(A+B)\cdot C_i$ ne moremo zamenjati s funkcijo XOR, saj nimata iste pravilnosnte tabele v primeru ko sta oba vhoda 1, vendar nas to ne briga saj _imamo pred tem clen $A \cdot B$ ki nam v tem primeru vedno da 1, torej napako lahko spregledamo_
|A|B|A xor B| A or B|
|-|-|-------|------|
|0|0|0|0|
|0|1|1|1|
|1|0|1|1|
|_1_|_1_|_0_|_1_|

- V vecbitnem sestevalniku _zakasnitev zaradi carry outa narasca linearno s stevilom bitov_
![[vecbitni_sestevalnik_zakasnitev.png]]

## Polni sestevalnik v izvedbi s komplementarnim CMOS
![[CMOS_sestevalnik.png]]

### Simetricnost funkcije
- lastnost funkcije, d je polovica njene pravilnostne tabele enaka negirani drugi polovici pravilnostne tabele
-  Ce negiramo vse vhode se bojo negirali tudi izhodi
![[simetricnost_vezave.png]]

- To lastnost lahko izkoristimo za pospesitev operacije
![[simetrija_pospesevanje.png]]
- Iz CMOS vezave odstranimo negatorja na izhodih $C_o$ in S, s tem prisparamo nekaj tranzistorjev in zakasnitev zaradi inverterja
	- Na prvem sestevalniku odstranimo negator na izhodu CARRY
	- Na drugem sestevalniku odstranimo negator na SUM izhodu
	- cikel se ponovi vsaka 2 sestevalnika

- Idealna tehnologija za izkoriscanje simetrije je _dinamicen cmos_

### Boljsa struktura: zrcalni sestevalnik
![[zrcaljeni_sestevalnik.png]]
- Vezje je simetricno, konfiguracija PMOS in NMOS sta enaki
- Nimamo inverterjev, zato smo prisparali 4 tranzistorje
- __Palicni diagram:__
![[palicni_diagram_zrcalni.png]]

- Vezavi _PMOS_ in _NMOS_ sta __zrcalni__
- V generatorju CARRY bita imamo najvec 2 zaporedno tranzistorja s cimer _drasticno zmanjsamo zakasnitev_ v primerjavi s komplementarnim CMOS
- Ko vezje sestavljamo je najbolj kriticen problem minimizacija kapacitivnosti v generatorju _carry out_
	- Sestavljena je iz:
	- _4 tranzistorjev_.  ki so vhodi za carry out
	- _2 internih gate_ kapacitivnosti na tranzistorjih, katerim $C_o$ predstavlja vhod
	- _6 gate kapacitivnosti_, iz sestevalnika, povezanega na $C_o$
- Tranzistorji povezani na $C_i$ so postavljeni cim blizje izhodu
- Samo tranzistorje na stopnji _carry out_ povecamo, ker je to najbolj hitrostno kriticen izhod
- Tranzistorji na stopnji sestevanja so lahko minimalne velikosti



### Polni sestevalnik, izvedba s prenosnimi vrati
![[sestevalnik_prenosna_vrata.png]]
- Izhoda P sta propagacijska, predstavlja XOR funkcijo
- Izhoda S in $C_o$ sta izvedena z _multipleksorjem_
- Vhod za S izhod oznacimo z X $$S = \bar{P} \cdot \bar{C_{in}}+P\cdot C_{in}$$
|$\bar{P}$|$\bar{C_{in}}$|X|
|-|-|-------|
|0|0|1|
|0|1|0|
|1|0|0|
|1|1|1|


### Manchester carry veriga
![[mancheste_carry.png]]
- Na vhode vezja peljemo nove spremenljivke stanja sestevalnika
	-  _Generate(G)_ = $A \cdot B$
	- _Propagate(P)_ = $A \oplus B$
	- _Delete(D)_ = $\bar{A}\cdot\bar{B}$
|G|D|P|$C_{out}$|
|-|-|-------|------|
|1|0|0|1|
|0|1|0|0|
|0|0|1|$C_{in}$|

- $\Phi$ nam predstavlja uro
![[manchester_carry_2.png]]
- V precharge fazi je $\Phi$ enak 0
	- Vsi carry biti so na 0, predstavlja stanje _delete_
- V fazi evaluacoje se zaprejo zgornji tranzistorji, povezani na Vcc in se odprejo sponji povezani na GND, $\Phi$ je 1
	-  Za stanje _generate_ se mora naboj iz prejsnje faze sprazniti na maso, to lahko stori prek razlicnih poti, od katere so nekatere daljse, nekatere pa krajse, pot je odvisna od stanja _vhodov G in P_
	- Za stanje _generate_ se $C_i$ preslika na C izhode prek _P tranzistorjev_
#### Palicni diagram
![[palicni_diagram_manchester.png]]


## Sestevalnik z obvodom carry bita
![[bypass_carry_addeer.png]]
- Da se vhodni carry _propagira_ na izhod morajo biti vsi _P vhodi na 1_
- Torej dodamo novo spremenljivko _BP_, ki je stirivhodna AND funkcija, katere vhodi so _P vhodi_, ko je ta spremenljivka 1 naredimo obvoz in carry peljemo direktno na zadnjo stopnjo
- V najslabsem scenariju se carry signal propagira cez _zadnje 3 sestevalnike_

- __16 Bitni sestevalnik, ki je sestavljen iz 4 bitnih blokov:__
![[continuous_carry_bypass_sestevalnik.png]]
(ignoriraj M bits pod prvim blokom)

- zakasnitev je sestavljana iz:
	- [[Predavanje NDES 8.12.2022#Setup time | Zakasnitve setup time]]
	- zakasnitve t carry, ki je pomnozena z _razmerjem stevila bitov_  __N__ in _stevila blokov_ __M__
	- zakasnitve t carry, ki je odvisna od stevila  ultipleksorjev __M__
	- in zakasnitve sestevanja t sum
- zakasnitev razlicnih sestevalnikov v razmerju s stevilom bitov:
![[primerjava_sest.png]]

## Sestevalnik "Carry select"
![[carry_select_sest.png]]

### Kriticna pot
![[kriticna_pot_carry_select.png]]
- v vseh stolpcih se ista vrstica izvaja istocasno

### Linearni carry select
![[linearni_carry_sest.png]]
- V casu 1 se hkrati izvedejo vse AND operacije za setup cikel
- V casu 5 dobimo izracunane carry bite 
- V casu 6 se rezultat _carry_ prenese na multipleksor v drugem stoplcu
- V casu 7 se rezultat _carry_ prenese na multipleksor v tretjem stoplcu
- V casu 8 se rezultat _carry_ prenese na multipleksor v cetrtem stoplcu
- V casu 9 se rezultat _carry_ prenese z multipleksorja v 4 stolpcu v generator SUM 4. stoplca
- _V casu 10_ na izhodu dobimo _rezultat_
- Najvec casa se porabi za _prenos med multipleksorji_
- Tej vezavi pravimo LINEAR ker zakasnitev linearno narasca s stevilom bitov, ki se enakomerno razdeli med posameznimi bloki

### Korenski carry select
![[korenski_carry_sest.png]]
(enacba je napacna, P bi moral biti N)

- na sestevalnik smo dodali se 4 bite, medtem ko smo pospesili delovanje za en cikel
- to smo dosegli s tem da smo dodajali bite na vsk blok, s cimer smo upocasnili racunanje carry in z njim _kompenzirali za zakasnitev multipleksorjev_ $$N = M+ M+1 + M+2 + M+3 + M+P-1$$
- N je stevilo bitov sestevalnika
- M je stevilo bitov v prvem bloku
- Pv je stevilo blokov
$$N = MP + \frac{P\cdot(P-1)}{2} = \frac{P^2}{2}+P\cdot(M-\frac{1}{2})$$
$$N \approx \frac{P^{2}}{2} \rightarrow P=\sqrt{2N} $$

$$t = t_{setup} + N\cdot t_{carry} + P\cdot t_{mux} + t_{sum}$$

### Primerjava zakasnitev setevalnikov
![[primerjava_zakasnitev.png]]



# Reference
# Tags
#ndes #adders #carry 