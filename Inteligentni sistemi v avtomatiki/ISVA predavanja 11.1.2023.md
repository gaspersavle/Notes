# Govorna komunikacija "človek - stroj“

11.01.2023
11:27
[[# Tags]]
[[# Reference]]

# Teme
- Sistem za govorno komunikacijo clovek-stroj
- Sistemi za dialog
	- Stanje razvoja na podrocju
- Gradniki sistema za govorno komunikacijo clovek-stroj
- Dialog clovek-stroj
- Turingov test
- Usmerjen dialog
- Nacini vodenja usmerjenega dialoga
- Upravljalec dialoga
	- Enota za pomensko obdelavo sporocil
		- Primeri pomenskih kategorij
	- Enota za generiranje sporocil
- Nacrtovanje sistema za dialog
- Simulacija carovnik iz oza
- Analiza gradiva zbranega s simulacijo dialoga

## Sistem za govorno komunikacijo “človek – stroj”
- cloveku omogoca dostop do aplikacij in/ali vodenje stroja
- gradijo se kot racunalniski sistemi za dialog
- pri interakciji lahko poleg govora uporabljamo:
	- _Za vhod:_
		- dotik
		- tipkanje
		- pisanje
		- geste
		- menijsko izbiranje
	- _Za izhod:_
		- zvok
		- grafika
		- animirani liki
		- svetila

## Sistemi za dialog
Poskusamo jih razviti kot _inteligentne avtonomne agente_, ki izvajajo naloge na podrocjih:
- podajanje informacij
- svetovanje
- izvajanje storitev
- oucevanje
- sodelovanje
- gospodinjenje
- tekmovanje
- varovanje
- pogovor

### Stanje razvoja na podrocju
Predvsem v tujini obstaja nekaj komercialnih sistemov, kot so:
- klicni centri
- govorno menijsko izbiranje storitev (rezervacije...)
- virtualni asistenti
- podpora soferju
- govorno vnasanje info v podatkovne baze
- ucenje jezika

## Gradniki sistema za govorno komunikacijo "clovek - stroj"
Glavni gradniki:
- razpoznavalnik govora
- sistem za dialog:
	- pomenski analizator
	- upravljalec dialoga
	- generateor sporocil
- sintetizator govora
![[zgradba_clovek_stroj.png]]

## Dialog "clovek-stroj"
- dialog je _vzajemni_ pogovor dveh ali vec oseb
- Locimo vec vrst pogovora:
	- _Spontani_ (ob kosilu...)
	- _Poucevalni_ (uscenje ucenca, instrukcije...)
	- _Usmerjeni_ (rezevacija sedeza...)
- Dialog clovek-stroj je navadno _usmerjen_


## Turingov test umetne inteligence
- Pogovor cloveka s prikritim strojem na eni strani ter clovekom na drugi strani
- Preizkus je uspesen, ce ne more ugotoviti kateri od sogovornikov ni clovek
- Stroj, ki zna simulirati cloveske navade ni nujno inteligenten
- Stroj bi lahko bil nadvse inteligenten, pa vendar nu smozen debatorati s clovekom
- Veliko manj izobrazenim ljudem bi spodletelo pri poskusu

- Predlagana zamenjava za Turingov test je _Winogradova shema_
 
![[primer_winograd.png]]


## Usmerjen dialog
- navadno modeliramo kot _avtomat stanje_
- ima _zacetno stanje_ in __vec__ _koncnih stanj_
- Dejanja stanja dialoga so SDA, UDA, IUDA
![[stanja_dialog.png]]


## Nacini vodenja usmerjenega dialoga
- Uprablja se vec nacinov vodenja usmerjenega dialoga, kot so enostavne menijske izbire, potrjevanje posameznih podatkov, potrjevanje izvedenih poizvedb, iniciativno vodenje, iniciativno vodenje in potrjevanje...

![[primer_vodenje_dialoga.png]]

## Upravljalec dialoga
- jedro sistema za dialog je _upravljalec dialoga_
-  Delovati mora smiselno in inteligentno
- __Naloge:__
	- sprejemanje pomensko obdelanih izjav uporabnika
	- ugotavlja spreminjanje stanja v dialogu
	- generiranje izjav sistema
	- napovedovanje naslednjih izjav uporabnika

### Enote za pomensko obdelavo sporocil
- Pomensko obdelana sporocila obdeluje _enota za pomensko analizo sporocil_
- V usmerjenih sistemih za dialog pomenska analiza sporocil pomeni iskanje besede ali fraz v vhodnem besedilu, ki predstavlja enoizmed podprtih _pomenskih kategorij_
- Obdelan stavek predstavimo s kljucnimi besedami, ki predstavljaji _govorno dejanje_ in vsebino , navadno oblikovoano kot seznam atributov in njihovih vrednosti

#### Primeri pomenskih kategorij
- __Govorna dejanja__:
	- pozdrav
	- poslovitev
	- zahteva
	- potrditev
	- zanikanje
- __Atributi:__
	- casovna kategorija
	- letalski prevoznik
	- mesto odhoda
	- mesto prihoda
	- ime letalisca

### Enota za generiranje sporocil
- Izhodna sporocila oz. izhodno besedilo oblikuje enota za _generiranje sporocil_ 
- Ta preslika _sistemska dejanja v dialogu_ v bsedilna sporocila v _naravnem cloveskem jeziku_
- Stevilo razlicnih sporocil je omejeno in navadno temelji na podlagi stavcnih predlog (sablon)

## Nacrtovanje sistema za dialog
- Poteka v vec fazah
![[nacrtovanje_sistema_za_dialog.png]]

## Simulacija carovnik iz oza
- Simulacijo delovanja sistema za dialog izvedemo po zgledi carovnika iz oza
- Uporabniki so prepricani,da se pogovarjajo z racunalniskih=m sistemom
- Sistem je delno pod kontrolocloveskega operaterja
- Dialogi izrazajo jezik komunikacij
- Pri uporabnikih se navadno opazi prilagajanje na jezikovne sposobnosti sistema, uporabo bolj artikularnega, pocasnejsega in glasnejsega govora
-  Cloveski operater izbira in prehaja med vnaprej izbranimi odzivi sistema ter rocno spreminja parametre simulacijskega odziva

## Analiza gradiva zbranega s simulacijo dialoga
- Z analizo zbranega gradiva s simulacijo dialoga dolocimo:
	- omejitev podrocja uporabe in izberemo cilje sistema
	- slovar in leksikon uporabljenega besedila
	- sestavitne pomenske analize uporabnikovi sporocil
	- uporabnikova in sistemska dejanja v dialogu
	- seznam zablon in pravil za tvorjenje sporocil sistema
- Zasnovo strukture uporavljanje dialoga navadno izvedemo s koncnim avtomatom stanje, obstajajo pa tudi drugi pristopi, kot polnjenje predalckov za vpogled v zbirko itd
- Preizkusanje sistema za dialog izberemo z _belezenjem dejanskih dialogov in oceno uspesnosti delovanje_



# Reference
# Tags
#isva #SpeechRecognition #HumanMachineCommunication