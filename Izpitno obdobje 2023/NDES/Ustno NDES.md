__Pohitritev signala z uporabo verige inverterjev (geometrično naraščanje pri dodajanju posameznih inverterjev)__

Velikost vsake stopnje inverterske verige je geometricna sredina njegovih 2 sosedov
$$C_{N} = \sqrt{C_{N-1} \cdot C_{N+1}}$$

__Izvedba inverterja v vseh tehnikah (statični CMOS, psevdo-NMOS, prenosna vrata, dinamični CMOS)__

_Prednosti/slabosti vsakega, hitrosti..._
- [[Predavanje NDES 1.12.2022#Staticna komplementarna CMOS logika|Komplementarni CMOS]]
	- visoke sumne meje
	- logicni nivoji so neodvisni od velikosti komponent _Ratioless_
	- v stabilnem stanju (ko ne poteka preklop) ima vedno povezavo na napajanje ali maso, ima  _Nizko izhodno impedanco_
	- _Izjemno visoka vhodna impedanca_, vhodni tok v staticnem stanju je skoraj nic
	- Nima _Staticne porabe moci_
	- Propagacijska zakasnitev je funkcija izhodne kapacitivnosti in upornosti tranzistorjev
	- Zaradi visoke uporrnosti _zaporedne vezave tranzistorjev_ nastopijo velike propagacijske zakasnitve pri visjem stevilu vhodov
	- _Pospesitvene tehnike:_
		- [[Predavanje NDES 1.12.2022#^3abab5 | Sekvencne velikosti tranzistorjev]]
		- [[Predavanje NDES 1.12.2022#^765712| Vhodna sekvenca]]
		- [[Predavanje NDES 1.12.2022#^e1c9bd| Alternativna struktura logike]]
		-  [[Predavanje NDES 1.12.2022#^badc8a| Izolacija FAN IN in FAN OUT vpliva]]
- [[Predavanje NDES 1.12.2022#^bbda7f|Psevdo logika]]
	- Zgrajena iz N-kanalnih tranzistorjev in upornega bremena s ciljem, da zmanjsa stevilo komponent (tranzistorjev) v primerjavi s komplementarnim CMOS
	- Izhodna napetost visokega stanja je enaka napajalni napetosti integriranega vezja
	- Izhodna napetost nizkega stanja je visja od potenciala GND, zaradi _padca napetosti na pull-up uporu_
	- Zaradi tega razloga ima ta tehnika tudi _staticno porabo moci_
	- Ta tehnika ima _asimetricen odziv_
- [[Predavanje NDES 8.12.2022#Prenosna vrata (transmission gates) | Prenosna vrata]]
	- Par vzporedno vezanih tranzistorjev, kjer je en izmed njih __P-kanalni z negiranim vhodom__ , __drug pa N-kanalni z nenegiranim vhodom__
	- Ker uporabljamo par nasprotnih tranzistorjev imamo lahko _hkrati mocno niclo in mocno enico_
- [[Predavanje NDES 8.12.2022#Dinamicna logika (dynamic logic) | Dinamicni CMOS]]
	- logicno funkcij implementiramo samo z uporabo PDN, porabimo manj tranzistorjev kot pri CMOS, saj moramo pri tisti tehniki PDN poustvariti z dualno vezavo PUN
	- _Full swing izhod_, $U_{OUT\space low} = GND$ in $U_{OUT \space high} = U_{DD}$
	- Non - ratioed, velikost gradnikov (tranzistorjev) ne vpliva na logicne nivoje vezave
	- Hitrejsi priklopi, kot pri staticnem CMOS
	- pri zaporedni vezavi logicnih vrat opazimo veliko manjso bremensko kapacitivnost $C_L$ zaradi manjsih vhodnih kapacitivnosti posameznih vrat
	-  Brez ztaticne porabe toka, zato je celotni tok, ki tece skozi PDN uporabljen za praznjenje izhodne kapacitivnosti $C_L$
	- Povprecna poraba _vecja, kot pri staticnem CMOS_
	- brez zstaticnega toka, saj ne obstaja prevodna pot med $U_{DD}$ in $GND$ 
	- brez _glitchinga_
	- _visje moznosti spremembe stanja_, kot pri staticnem CMOS
	- dodatna obremenitev _CLK_
	- PDN se odzove takoj, ko vhodni signali presezejo kolensko napetost tranzistorjev, torej velja $$U_{TN} = U_{M} = U_{IN high} = U_{IN low}$$
		- iz tega sledi, da ima ta tehnologija nizko sumno mejo
	- potrebuje urni signal

__Zakaj uporabiti domino izvedbo pri kaskadah elementov (kako vpliva na sosednje elemente)__
- Pri navadnem dinamicnem CMOS se lahko pri kaskadah elementov zgodi, da _polnilna faza enega elementa povzroci predcasno praznjenje izhodne kapacitivnosti sosednjih elementov_
- Pri domino logiki med kaskadna dinamicna vrata vezemo _inverterje_, s tem se izognemo predcasnemu praznjenju kapacitivnosti naslednje stopnje
- imenujemo jih domino, saj vsaka stopnja posreduje svoj izhod naslednji za evaluacijo
- _implementiramo lahko_ __le neinvertirajoce__  _funkcije_
- zelo visoka hitrost preklapljanja
	- inverterje med stopnjami lahko asimetricno dizajniramo, torej P-kanalnega tranzistorja ni treba povecati, saj bo inverter opravljal le prehod  1 na 0
	- zmanjsana kapacitivnost in posledicno manjsi trud logike

__Inverter in karakteristika inverterja__

- _Prenosna karakteristika inverterja_
![[Pasted image 20230125230053.png]]

__Dinamicna poraba inverterja__
- Ni odvisna od velikosti tranzistorjev
- Energija je porabljena za _polnjenje bremenske kapacitivnosti_
- Za zmanjsanje porabe moramo zmanjsati fanout, bremensko kapacitivnost $C_{L}$ in napajalno napetost $V_{DD}$ 
- Kratki stik med preklopom
- Puscanje na maso zaradi vhodnega stanja pod preklopno mejo
__Kaksne so sirine kanalov v staticnem CMOS__
![[Pasted image 20230126124032.png]]
- S sirsim kanalom pospesimo odziv inverterja.
- Zaradi manjse gibljivosti vrzeli, ima _PMOS_ pocasnejsi odziv od NMOS, zato moramo naraditi kanal PMOS _3x sirsi od NMOS_, da dobimo simetricen odziv

__Kakšna je razlika med linearnim in kvadratno korenskim carry selectom kateri od njiju je hitrejši in zakaj__

[[NDES predavanje 22.12.2022#Linearni carry select | Linearni Carry Select]]
linearni carry select ima v vsakem stoplcu enako stevilo bitov, _zakasnitev narasca linearno z dodajanjem novih bitov_

[[NDES predavanje 22.12.2022#Korenski carry select | Korenski Carry Select]]
Bottleneck linearnega carry selecta je cakanje prenosa carry bita med multipleksorji, zato smo v vsak naslednji stoplec dali vec bitov, tako bolje izkoristimo cas, ki bo porabljen za prenos carry bitov. Zakasnitev tega tipa carry selecta _narasca kvadratno korensko s stevilom bitov_
![[primerjava_zakasnitev.png]]

#ndes #izpitno2023  #ustno 