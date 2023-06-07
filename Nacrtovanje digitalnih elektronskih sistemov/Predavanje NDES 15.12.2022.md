
15.12.2022
14:12
[[# Tags]]
[[# Reference]]

# Teme
- Preboj povratne vezave s krizno vezanimi pari vrat
	- vpliv geometrije na logicne nivoje in propagacijske case
	- spominski mehanizmi
	- natancnejsi setup time
- Drugi zapahi/registri _C^2 MOS_
	- prekrivanje ure 0-0
	- prekrivanje ure 1-1
	- pipelining
- Drugi zapahi/registri _TSPC register_
	- osnovno
	- vkljucevanje logike v TSPC
	- TSCP register
- Pulzno prozeni zapahi
	- generacija impulza CLKG
- Cevovod na podlagi zapahov
- Ne-bistabilna sekvencan vezja - Schmittov prozilnik
	- CMOS izvedba
- Multivibratorji
	- Frontno prozeno monostabilno vezje
	- Monostabilni prozilnik na bazi RC vezja
	- Nastavljivi multivibratorji
	- Relaksacijski oscilator
	- Napetostno krmiljen oscilator

## "Preboj" povratne vezave, krizno vezani pari
- par negatorjev razsirimo z dodatnima vhodoma _S in R_
	- mozna izvedba z vrati _NOR_ ali _NAND_
	- v vezavi z _NOR_ morata biti oba dodatna vhoda na 0, za delovanje ekvivalentno paru negatorjev
-  __Izvedba z NOR:__
![[SR_NOR.png]]
- __Izvedba z NAND:__
	- v vezavi z _NAND_ morata biti za delovanje enako paru negatorjev morata biti oba dodatna vhoda na 1, da vezje _vzdrzuje stanje_
	- za spremembo stanja mora sprememba na enem izmed vhodov trajati vsaj toliko, kot zakasnitev vezja, kar je v obeh izvedbah zakasnitev para vrat
| S | R | Q | !Q |
|--|--|--|--|
| 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 0 |
![[SR_NAND.png]]
- __Izvedba  NOR SR s tranzistorji:__
![[NAND_SR_tranzistorji.png]]
- ce pogledamo samo eno stran vezja nas zelo spominja na __PSEVDO NMOS__ oziroma [[Predavanje NDES 1.12.2022#Psevdo NMOS | RATIOED LOGIC]]
- zato je zelo pomembno dimenzioniranje tranzistorjev _M5 in M6_
### Vpliv geometrije
![[vpliv_geometrije.png]]
- grafa prikazujeta logicne nivoje v odvisnosti od _sirine vrat tranzistorjev M5 in M6_
	- levi graf prikazuje logicni nivo __Izhodne napetost__
	- desni graf prikazuje odzivne case SR vrat v odvisnosti od sirine tranzistorja, pri preozkih tranzistorjih vidimo celo, da se __preklop sploh ne zgodi__ zaradi premocne povratne vezave
	- vedenje vezja je zelo odvisno od razmerja P in N kanalnih tranzistorjev v posamezni strani vezja
	
### Spominski mehanizmi
![[spominski_mehanizmi.png]]

### Natancnejsi setup time
- s krajsanjem [[Predavanje NDES 8.12.2022#Setup time|setup time-a]] vecamo casovno konstatno preklopa izhodnega signala, v primeru ko je prekratek se naboj ne uspe prenesti do zadostne mere in se _preklop sploh ne zgodi_
![[ilustracije_setup_time.png]]

![[ilustracije_setup_time_2.png]]
![[setup_time_3.png]]
![[Pasted image 20221215153320.png]]
![[Pasted image 20221215153332.png]]
![[Pasted image 20221215153344.png]]

## Drugi zapahi / registri: C^2 MOS
- $C^{2}MOS$
- vezje je neobcutljivo na prekrivanje urinega signala
![[c_2_MOS.png]]
- implementiramo t.i. _Keeperje_, da vezje naredimo psevdo-staticno, _Keeperja_ sta dodatna P in N tranzistorja, ki ju vkljucimo v standardno CMOS invertersko vezavo
### Prekrivanje 0-0
![[prekrivanje_00.png]]
- ko sta oba urna signala v 0, se prekrivata in tranzistorja M3 i M7 sta zaprta,  zato preoblikujemo vezje
- vhod se nikakor ne more preslikati na izhod, kar je nas cilj
### Prekrivanje 1-1
![[prekrivanje_11.png]]
- ko sta oba urna signala 1 sta tranzistorja M4 in M8 zaprta
- vhod se nikakor ne more preslikati na izhod

### Cevljenje - PIPELINING
![[pipelining.png]]
- v prvi, levi shemi je maksimalna urna frekvenca odvisna od zakasnitve vseh operacij na poti do registra
- v drugi, levi __CEVLJENI__ shemi je maksimalna urna frekvenca odvisna _le od zakasnitve ene same operacije_, saj se po vsaki operaciji vrednost spet shrani v register, v tem primeru lahko z uporabo cevovoda frekvenco ure _potrojimo_


## Drugi zapahi / registri: TSPC
- _True Single Phase Clock_
- __Pozitiven zapah:__
![[pozitiven zaoah.png]]
- prevaja samo ko je urni signal na 1, sicer vhodna vrednost v nobenem primeru ne pride mimo drugih vrat, v vecini primerov pa niti skozi prva
- __Negativen zapah:__
![[negativen_zapah.png]]
- prevaja samo ko je urni signal 0, sicer se vh ne prenese na izh

### Vkljucevanje logike v TSPC
![[logika_TSPC.png]]
- logiko smo vkljucili naravnost v zapah, vezje na sliki se obnasa kot zapah ce je CLK v 0, sicer pa se vezje obnasa, kot AND vrata


### TSCP register
- vezje __vsebuje le pozitiven urin signal__
- torej je to _prava enofazna ura_
![[tscp_register.png]]
- ce na izhod vezja dodamo se _povratno vezavo_, poskrbimo, da se bo vredost ohranjala tudi, ce se urni signal ne bo osvezeval
	- to dosezemo z dodajanjem se enega negatorja v nasprotni smeri, kot izhodni negator
1. __Prehod D iz 0 v 1:
	- ura je v 0, torej je _M2 odprt_
	- _M3 je zaprt, M1 je odprt_, torej je _Izhod X v 0_
	- _M6 je odprt, M4 pa zaprt_, torej je _Y v 1_
	- ker je Y v 1 je _M9 zaprt, M7 pa odprt_
2. __Prehod D iz 1 v 0:
	- M3 se odpre, torej se _X spremeni v 1_
	- Y ostane v 1, vendar se zaradi nove vrednosti ure _Odpre M8_, kar vodi v praznjenje izhoda na 0, torej na _izhodu dobimo 1_

- _CLK = 0 & D = 0:_ 
	- M2 je odprt, M3 je odprt -> __X = 1__
	- M5 je odprt, M6 je odprt -> __Y = 1__
	- M9 je zaprt, M8 je odprt, vendar ne spremeni nicesar, saj je M8 zaprt zaradi ure na 0, torej __se ohranja prejsnje stanje__
- _CLK = 1 & D = 0:_ 
	- M3 je odprt, vendar to nicesar ne spremeni, saj je M2 zaprt zaradi CLK na 1, __X ostane na prejsnji vrednosti, X = 1__
	- ker je X = 1 je odprt M5, M4 pa prav tako, torej se __Y izprazni na 0__
	- Y = 0 odpre tranzistor M9, torej __se izhod postavi na 0__
- _CLK = 1 & D = 1:_
	- D = 1 pomeni, da se odpre M4, prek katerega se __spremenljivka X sprazni na 0V__
	- M5 je zaprt, ker je X = 0, torej __Y ohranja prejsnjo vrednost, torej 0__
	- ker je Y = 0, je M9 zaprt, torej izhod ohranja prejsnje stanje
- _CLK = 0 & D = 1:_
	- M2 in M4 sta odprta, __X = 0__
	- ker je CLK = 0, se odpre M6, kar __vrednost Y napolni na 1__
	- izhod __ohrani prejsnje stanje__

- Pred preklopom D moramo pocakati, da se sprazni naboj na spremenljivki X
- pri prehodu D iz 0 v 1 je $t_{SU}$ odvisen od prehoda X z 0 na 1, CLK-Q delay pa je pogojevan s casom praznjenja _! Q_ in casa polnjenja _Q_
	- zaradi slabse prevodnosti p tranzistorja bo ta prehod zahteval _daljsi hold delay in CLK-Q delay bo tudi vecji_
- privprehodu D z 1 v 0 je setup time ovisen od casa polnjenja naboja na spremenljivki X, CLK-Q delay pa je odvisen od _polnjenja ! Q_ in _praznjenja Q_

## Pulzno prozeni zapahi
![[pulzni_zapahi.png]]
- s krajsanjem urinega signala zmanjsamo cas transparentnosti in zmanjsamo vpliv hitrih sprememb vhoda D
### Generacija kretkega urinega impulza
![[generacija_clkg.png]]
- ko je CLK v 0 je vmesna vrednost X v 1, vendar na izhodu CLKG vseeno 0,, kar bo drzalo vrednost X na 1
- v primeru _ko ura preide v 1_ se trranzistor Mp zapre, , torej X ostane v 1 in odpre Mn, ter posledicno _samega sebe sprazni_, torej je trajanje CLK pulza _odvisno od casa praznjenja X, zakasnitve AND vrat in 2 negatorjev_

## Cevovod na bazi zapahov
![[cevovod_zapahi.png]]

## Ne-bistabilna sekvencna vezja - Schmittov prozilnik
![[schmitt.png]]
- uporaben za odpravljanje suma, npr. pri ogrevanju, saj bi se sicer ogrevanje vklapljalo takoj, ko nam temp. pade pod ciljno. sistem bi zacel nihati.
### Izvedba s CMOS
![[cmos_schmitt.png]]
- pri _prehodu vhodne napetosti z 0 na 1_ se vmesni signal _X s prvotne vrednosti 1 sprazni prek odpretega tranzistorja M1_, ko X doseze 0 se bo zaprl tranzistor M4 in odprl tranzistor M3, torej imamo odprta 2 tranzistorja N tipa, kar pomeni, da __smo preklopno napetost za prehod izhoda z 1 na 0 premaknili nizje__, saj smo spremenili razmerje P in N tranzistorev. Z vzporedno vezavo 2 N tranzistorjev smo efektivno podvojili sirino N kanala
- pri _prehodu vhoda z 1 na 0_ se vmesni signal X _napolni prek odprtega tranzistorja M2_, ko le-ta doseze vrednost Udd/2 _se izhod zamenja na 0_, kar posledicno _odpre M4 in zapre M3_, torej smo dobili 2 vzporedno vezana P tranzistorja in s tem efektivno podvojili njuno sirino, __preklopno napetost izhoda z 0 na 1 premaknili visje__
- s tem dosezemo, da imamo za prehode med izhodnimi logicnimi nivoji __razlicne preklopne napetosti__, kar vidimo na _naslednjem grafu:_
![[prenosna_karakteristika_schmitt.png]]
- K nam predstavlja razmerje $\frac{P}{N}$

## Multivibratorska vezja
![[multivibratorji.png]]
### Frontno prozeno monostabilno vezje
![[edge_monostable.png]]
- izhod vezja je vedno 0 _razen v casu td po prehodnem pjavu_

### Monostabilni prozilnik na bazi RC vezja
![[rc_monostable.png]]
- do trenutka, ko nastopi pulz _je tocka A v stanju 1, saj je B na 1 zaradi Udd_
- ko nastopi pulz se napetost A _spremeni v 0_, _B pa tudi v 0_, izhod se _postavi na 1_
- ko vhod spet pade na 0 se bo najprej _napetost B dvignila do Udd/2_, kar bo na izhod postavilo vrednost 0, ki bo _posledicno napetost v tocki A postavila nazaj na 1_
- cas trajanja izhodnega impulza je odvisna __od casovne konstante RC clena na tocki B__, saj nam ta konstanta narekuje _koliko casa bomo potrebovali, da tocka B doseze vrednost Udd/2_


### Prilagodljivi multivibratorji (oscilatorji)
- izvedemo ga z lihim stevilom negatorjev
![[pril_multivib.png]]

### Relaksacijski oscilator
![[rel_osc.png]]
- OUT1 in OUT2 sta v _protifazi_
- v casu ko je napetost v tocki Uout 1, bo potencial v tocki int _manjsi od Udd/2_
- ko doseze napetost Udd/2 bo to obrnilo stanje prvega negatorja, torej bo potencial v tocki OUT1 padel na 0, v tem casu se bo UOT2 _postavil na 1_, potencial na vozliscu _INT pa se postavi na vrednost:_ $3\cdot \frac{U_{DD}}{2}$
- ko bo OUT2 v 1 bo napetost v tocki _INT padala na vrednost Udd/2_, ko jo doseze se spet obrne stanje na prvem inverterju in posledicno na drugem, torej velja: _OUT1 je 1, OUT2 pa 0_, takrat napetost INT _pade na -Udd/2_
- po obratu stanja na inverterjih napetost na INT _konvergira proti Udd_, dokler ne doseze _Udd/2_, ko vezje spet preklopi stanje in _se cikel ponovi_
- __Duty cycle je 50%__


### Napetostno krmiljen oscilator (VCO)
![[vco.png]]
- z vecanjem $U_{cont}$ lahko vecamo I ref, s cimer vplivamo na hitrost preklopa schmitovega prozilnika
![[vco_prenosna.png]]


# Reference
[[Predavanje NDES 1.12.2022]]
# Tags
#ndes #latch #cmos #tscp #oscilators #clockPulse #schmittTrigger #oscilators 