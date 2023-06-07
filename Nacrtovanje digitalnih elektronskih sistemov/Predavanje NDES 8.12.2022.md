09.12.2022
18:39
[[# Tags]]
[[# Reference]]

# Teme
- Pass transistor logic, __logika prenosnih vrat__
	- Izvedba samo z NMOS
	- Popravljalnik logicnih vivojev
	- Komplementarna logika prenosnih vrat
	- Prenosna vrata
	- Multipleksor na bazi prenosnih vrat
- Dynamic logic, __Dinamicna logika__
	- Dinamicen CMOS
	- Dinamicna vrata
		- Izvedba s P
		- Izvedba z N
	- Izhodni pogoji
	- Lastnosti dinamicnih vrat
	- Problemi dinamicnih vrat
	- Kaskadna dinamicna vrata
	- Domino logika
- Sekvencna logika
	- poimenovanje
	- zapah/register
	- zakasnitve
	- maksimalna urna frekvenca
	- bi-stabilnost
	- zapahi na bazi multipleksorjev
	- Pisanje v staticen zapah
	- Master-slave register
	- Cas postavitve
	- Zmanjsana urna obremenitev
	- Prekrivanje ure
## Logika prenosnih vrat (pass transistor logic)
- manjse stevilo gradnikov, za N vhodov potrebujemo N tranzistorjev
- brez staticne porabe moci
- __Primer, AND vrata:__
![[PTL_AND.png]]
### Izvedba samo z NMOS
![[NMOS_only_PTL.png]]
- napetost X nikoli ne doseze vrednosti $U_{DD}$, saj je napetost $U_{GS}$ manjsa od kolenske napetosti tranzistorja $U_T$ , torej lahko napetost x doseze le vrednosti: $$X = U_{DD} - U_T$$
- zaradi prenizke napetosti X je P-kanalni mosfet v inverterju nekoliko odprt, kar povzroci porabo moci v staticnem stanju
![[staticna_poraba_PTL_nmos.png]]
- za popravljanje te hibe PLT uporabljamo __popravljalnik logicnih nivojev__ oziroma _level restoring transistor_
### Popravljalnik logicnih nivojev (level restoring transistor)
- __PREDNOSTI:__
	- full swing - nisoko izhodno stanje logicnih vrat je enako napajalni napetosti, medtem ko je nizko stanje enako zameljskemu potencialu GND, vezje torej izkoristi cloten razpon napajalne napetosti
- popravljalnik doda dodatno kapacitivnost, saj predstavimo v vezje nov tranzistor, ta kapacitivnost nam "odvzame" nekaj pull-down toka, torej toka s katerim praznimo bremensko kapacitivnost, saj se del toka izgubi na novi kapacitivnosti popravljalnika
- paziti moramo na razmerje $M_r$ in $M_n$ , ce bo popravljalnik prevelik se bremenska kapacitivnost nikoli ne bo povsem izpraznila
- __HItrost praznjenja bremenske kapacitivnosti glede na velikost popravljalnika__ , oziroma hitrost prehoda izhodnega stanja z 1 na 0
![[hitrost_odvisna_od_velikosti_popravljalnika.png]]
### Komplementarna logika prenosnih vrat
![[komplementarni_PTL.png]]
- alternativa za komplementarni CMOs z manjso porabo tranzistorjev, namesto se enega para dualno veznih tranzistorjev uporabljamo se en par, ki je vezan enako, vendar z negiranimi vhodi.
- __Primeri komplementarne PTL:__
![[komplementarni_PTL_primeri.png]]
### Prenosna vrata (transmission gates)
- par vzporedno vezanih tranzistorjev, kjer je en izmed njih __P-kanalni z negiranim vhodom__ , __drug pa N-kanalni z nenegiranim vhodom__
- ker uporabljamo par nasprotnih tranzistorjev imamo lahko _hkrati mocno niclo in mocno enico_
![[transmission_gate.png]]
- na primeru je razvidno, da je: $A = B$ samo, ce velja: $C = U_{DD}$
#### Upornost prenosnih vrat
![[upornosti_prenosnih_vrat.png]]
#### Multiplekser na bazi prenosnih vrat
![[mux_prenosna_vrata.png]]
- s tako vzporedno vezavo prenosnih vrat lahko naredimo zelo enostaven __input switcher__


## Dinamicna logika (dynamic logic)
- v _staticnih_ vezjih smo v kateremkoli trenutku (izven preklopa) povezani na napajanje ali maso prek nizkoimpedancne poti
	- za fanout __n__ potrebujemo __2n__ tranzistorjev, ( __n__ X _N-tip_ + __n__ X _P-tip_)
- v _dinamicnih_ vezjih se zanasamo na zacasno shranjevanje signalnih vrednosti na interne kapacitivnosti visokoimpedancnih clenov
	-  za fanout __n__ potrebujemo le __n+2__ tranzistorjev, ( __(n+1)__ X _N-tip_ + __1__ X _P-tip_)
- dinamicna logika deluje v __2 urinih ciklih:__
	- _precharge_ - polnilni cikel (CLK = 0). V tem ciklu se napolni izhodna kapacitivnost naravnost z $U_{DD}$, po zalugi polnilnega tranzistorja $M_p$
	- _evaluate_ - evaluacijski cikel (CLK = 1). V tem ciklu se sklene stik logicnih vrat na maso prek evaluacijskega tranzistorja $M_e$, pri tem se "preveri", ce je izhodna vrednost dejansko 1, ali se bo prek evaluacijskega tranzistorja spraznila na maso

![[dinamicna_vrata.jpg]]
![[prenosna_vrata_delovanje.png]]
### Izhodni pogoji
- Ko je izhod dinamicnih vrat izpraznjen, ga _ne moremo znova napolniti do naslednjega polnilnega cikla_
- vhodi v dinamicna vrata lahko opravijo __LE en__ prehod med evaluacijo
- izhod je lahko _v visokoimpedancnem stanju_ med ali po avaluaciji, (PDN je izklopljen), __stanje je shranjeno na izhodni kapacitivnosti__ $C_L$
### Lastnosti dinamicnih vrat
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
### Problemi dinamicnega CMOS
#### Puscanje naboja
- ker ura nima perfektnega pravokotnega signala, tranzistorja nekaj casa prezivita v napol odprtem stanju, zaradi tega nekaj naboja iz bremenske kapacitivnosti pusca skozi maso
![[puscanje_naboja_dynamic_CMOS.png]]
- resitev za puscanje navoja je popravljalnik logicnih nivojev, ki bo dokler je izhod na 1 dovajal nov naboj v izhodno kapacitivnost naravno z napajalne napetosti
![[popravljalnik_nivoja_dinamicen_CMOS.png]]
### Kaskadna dinamicna vrata
- zaradi kolenske napetosti tranzistorja $U_T$ , out1 nikoli ne doseze popolne nicle, kar se potem odraza tudi na out2 in tako naprej po verigi, zato so v kaskadnih dinamicnih vratih _dovoljene le negativne fronte na vhodih_ 
![[kaskadna_dinamicna_vrata.png]]
### Domino logika
- pri domino logiki med kaskadna dinamicna vrata vezemo _inverterje_, s tem se izognemo predcasnemu praznjenju kapacitivnosti naslednje stopnje
- imenujemo jih domino, saj vsaka stopnja posreduje svoj izhod naslednji za evaluacijo
- _implementiramo lahko_ __le neinvertirajoce__  _funkcije_
- zelo visoka hitrost preklapljanja
	- inverterje med stopnjami lahko asimetricno dizajniramo, torej P-kanalnega tranzistorja ni treba povecati, saj bo inverter opravljal le prehod  1 na 0
	- zmanjsana kapacitivnost in posledicno manjsi trud logike
![[domino_logika_1.png]]
![[domino_logika_2.png]]
### Diferencialna (dual rail) domino logika
- resi problem invertirajocih funkcij
![[diferencialna_domino_logika.png]]
- __DOPOLNI__
### NP-CMOS
- __DOPOLNI__
![[NP_CMOS.png]]
### NORA logika
- __DOPOLNI__

![[NORA_logika.png]]
## Nacrtovanje sekvencnih logicnih vezij
### Sekvencna logika
- kombinacijska logika s povratno zanko, se zaveda svojega prejsnjega stanja
- pri enaki kombinaciji vhodov ni nujno enak izhod
![[sekvencna_logika.png]]
- poznamo 2 mehanizma _hrambe stanja:_
	- pozitivna povratna zanka
	- na bazi naboja
### Poimenovanje
- __Zapah__ (latch) je obcutljiv na logicne nivoje
- __Register__ (register) je obcutljiv na fronte (falling edge, rising edge)
- elementom, ki jih prozijo fronte pravimo tudi _Flip-flopi_
### Primerjava zapah-register
- Zapah hrani podatke, ko je _urni signal na nizkem stanju_
- Register hrani podatke, _ko se urni signal "dvigne"_
![[zapah_proti_register.png]]
### Zapahi
- poznamo pozitivne in negativne zapahe, negativni imajo _negiran vhod za urni signal_
![[pozitivni_negativni_zapah.png]]
### Dizajn na bazi zapahov
- izraz __Transparentnost__ nam pove, da izhod zapaha sledi njegovemu vhodu
	- _N_ zapah je transparenten, ko je ura na __visokem stanju__
	- _P_ zapah je transparenten, ko je ura na __nizkem stanju__
![[dizajn_na_bazi_zapahov.png]]

### Maksimalna urna frekvenca
- minimalna perioda ure je pogojena s tremi parametri
	- __Setup time:__ $t_{SU}$ je _cas, ki potece od spremembe na vhodu D do pozitivne fronte ure_ [[#Setup time]]
	- __Combination time:__ $t_{COMB}$ je _zakasnitev kombinacijskega dela vezja_ in je odvisen od notranjih komponent in tehnologije izdelave kombinacijskega vezja
	- __CLK-Q zakasnitev:__ $t_{CLK-Q}$ je _zakasnitev med pozitivno fronto ure in odzivom izhoda registra_ [[#CLK - Q zakasnitev]]
![[maksimalna_urna_frekvenca.png]]
![[definicije_zakasnitev.png]]
### Pozitivna povratna zanka, bi-stabilnost
![[bistabilnost_sekvencna_vezja.png]]
### Zapahi na podlagi multipleksorjev
- dvovhodne multipleksorje lahko uporabimo za izdelavo zapahov tako, da izhod povezemo na zeleni vhod ter urni pulz povezemo na selekcijski vhod multipleksorja
![[mux_latches.png]]
### Pisanje v staticen zapah
- uporabimo _PTL_ oziroma [[#Prenosna vrata (transmission gates)|logiko prenosnih vrat]]
- iz prenosnih vrat lahko tvorimo [[#Multiplekser na bazi prenosnih vrat]]
- Urni signal povezemo na PTL in se tako odlocamo med _transparentnostjo_ ali _zadrzevanjem_
- _Zadrzevanje_ realiziramo z zadrzevalnikom logicnega nivoja
	- ce povezemo 2 logicna inverterja enega v drugega se temu rece _zadrzevalnik logicnega nivoja_
![[pisanje_v_staticen_zapah.png]]
### Master-slave register
- ko zaporedno vezemo 2 _nasprotna zapaha_ se prozita samo ob fronti, temu pravimo __master-slave register__
![[master_slave_registere.png]]
![[master_slave_register_2.png]]
### CLK - Q zakasnitev
- CLK-Q zakasnitev je lastnost registra, ki ga uporabljamo in je _zakasnitev med pozitivno fronto  CLK in preslikavo vhoda D na izhod Q_
![[clk_q_zakasnitev.png]]
### Setup time
- setup time je _cas, ki mine od trenutka, ko smo na vhod D pripeljali visoko stanje, do trenutka, ko napoci pozitivna fronta CLK_
![[setup_time.png]]
### Zmanjsanje obremenitve ure
- namesto, da bi pri _master-slave_ registru uporabljali dvojna prenosna vrata, eliminiramo vrata za povratno zanko in __inverterje zadrzevalne vezave vezemo direktno skupaj__
- pri paru smo tako s 4 prenosnih vrat presli na dvoje prenosnih vrat, torej smo _razpolovili urino obremenitev_
![[zmanjsanje_urine_obremenitve.png]]
- upostevati moramo, da bodo vsaka prenosna vrata v novonastali vezavi morala _"premagati" logicni nivo ohranjevalnika_, zato __inverterja i2 in i3 naredimo manj zmogljiva__

### Prekrivanje urinega signala
- ker za prozenje registrov in zapahov uporabljamo neobdelan in _invertiran urin signal_ ima invertiran dodatno zakasnitev, saj mora potovati skozi dodatne gradnike
- zaradi prikrivanja urinega signala sta _oba zapaha v transparentnem stanju_, torej v trenutku prikrivanja urninih signalov __obstaja prevodna pot med D in Q__, torej se _izhod lahko spremeni tudi ob negativni fronti CLK_
![[prekrivanje_urinega_signala.png]]

# Reference
https://ece.uwaterloo.ca/~mhanis/ece637/lecture15.pdf
# Tags
#ndes #chip #cmos #dynamicCMOS #passTransistorLogic #PTL #sekvencnaVezja