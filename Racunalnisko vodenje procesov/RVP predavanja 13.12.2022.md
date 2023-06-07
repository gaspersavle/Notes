
14.12.2022
22:13
[[# Tags]]
[[# Reference]]

# Teme
- Prakticni problemi realizacije regulacije
	- filtriranje
	- preklop rocni-avtomatsko
	- zascita pred _integralskim pobegom_
- Konfiguracija in parametriranje industrrijskih regulatorjev
	- programska orodja
	- samodejno parametriranje
- Regulator __SIPART DR24__
	- funkcije
	- regulacijske funkcije
	- programiranje
- nadzorni sistemi

## Prakticni problemi regulacijskih algoritmov
- regulacijski algoritem predstavlja _le del programa industrijskega regulatorja_
- Pojava motenj na vhodnih signalih
- Razlicni rezimi obratovanje, poseg operaterjev v delvanje regulatorja
- Integralski pobeg

### Filtriranje
- S filtriranjem lahko izlocimo motnje na vhodnih signalih
- Te motnje lahko klasificiramo v __2 razreda__
	1. _Frekvence, ki krsijo teorem vzorcenja_
	2. _Šumi_
#### Frekvence, ki krsijo teorem vzorcenja
- visokofrekvencne motnje se preslikajo v nizkofrekvencne
-  pred vzorcenjem signala, ga je potrebno filtrirati, to izvedemo z _zveznimi filtri_
![[zvezno_filtriranje.png]]
#### Izločanje šuma
- vzorcni signal filtriramo z digitalnimi filtri
#### Primeri
1. __Origninalni signal 1 Hz, motnja 50 Hz, vzorcna frekvenca 16 Hz:__
	 ![[vzorceni_signal_z_motnjo.png]]
2. __Vzorcen vhodni signal:__
![[vzorcen_signal_z_motnjo.png]]
- _50 Hz motnja se je preslikala v 2Hz motnjo_
3. __Filtriran signal, filter 2. reda, mejna frekvenca je 10 Hz:__
![[filtriran_signal_z_motnjp.png]]
4. __Filtriran IN vzorcen signal:__
![[filtriran_in_vzorcen_signal.png]]
### Preklop rocno - avtomatsko
1. __Rocni nacin:__  Operater proces vodi z nastavljanjem regulirne velicine preko uporabniskega vmesnika, proces si razdeli na vec delov:
	- zagon procesa
	- zaustavitev procesa
	- sprememba obratovalnega rezima
2. __Avtomatski nacin:__ Vrednosti sistema se gibljejo le v okolici delavne tocke, regulator ni sposoben samodejnega zagona in izklopa procesa brez zunanjega navodila
- Pri preklopu med obratovalnima nacinoma ne sme priti do prevelike spremembe regulirne velicine
- V trenutku preklopa, morata biti operaterjeva in regulatorjeva regulirna velicina priblizno enaki
#### Izvedbe
![[izvedbe_preklopa_rocno-avtomatsko.png]]
### Zascita pred integralskim pobegom
- Poglavitni vzrok integralskega pobega je _omejeno podrocje delovanja cleniov regulatorja_ 
	- Regulina velicina, ki jo vidi proces zaradi omejitev ne narasca tako hitro, kot pricakuje regulator, torej pogresek pada pocasneje, kot regulator predvideva
	- integral pogreska je zato vecji, izhod i clena pa nekontrolirano naraste. tudi, ko je pogresek ze negativen, se regulirna velicina zato ne more takoj zmanjsati, torej izvrsni clen __ostane v nasicenju__
	- povzroca _velik prevzpon pri prehodnem pojavu_
- _Potrebno je omejiti izhod integrirnega clena_


1. __Omejitev s povratno zanko__
![[povratna_zanka.png]]
- v vezje vgradimo _kompenzator integralskega pobega_, ta omeji izhodno vrednost povratne zanke, ko izvrsni clen _doseze nasicenje_, tako integratorju prepreci nadaljno dviganje izhodne vrednosti, s tem da __mu omeji vhodno__
2. __Upostevanje dejanskega izhoda izvrsnega clena__
![[upostevanje_dejanskega_izhoda.png]]
- namesto, da bi integrirni clen v povratni zanki dobival informacijo o _regulirni velicini_, dobi informacijo o dejanski izhodni velicini izvrsnega clena, tako preprecimo prevelik prenihaj
![[preimer_brez_kompenzacije.png]]
- vijola in oranzen signal predstavljata vrednosti pred kompenzacijo, _moder in rumen signal pa predstavljata vrednosti po kompenzaciji_
## Konfiguracija in prametriranje
- Lahko jo izvedemo prek:
	- Celne plosce
	- Prenosnih terminalov
		- Omogoca vnasanje sprememb na mestu vgradnje
		- Zamudno in nepregledno
	- Z osebnim racunalnikom
		- Uporabniku prijazno (debatable)
### Programska orodja
- vezana na specificen tip regulatorja
- graficni uporabniski vmesnik
- blokovne sheme
- prenos parametrov in nastavitev v regulator
- avtomatska generacija dokumentacije
- spreminjanje poteka signalov v regulatorju
- spreminjanje parametrov med samim delovanjem

### Samodejno parametriranje
- Poznamo vec postopkov samodejnega parametriranje
	- Auto - tune
	- metoda spremenljivega parametra (gain scheduling)
	- avtomatsko prilagajanje (adaptive control)
		- nenehno prilagaja parametre spremembi dinamike
		- slaba stabilnost
#### Avtomatsko nastavljanje
![[autotune_siemens.png]]
- __Postopek:__
	1. dolocanje parametrov postopka nastavljaja
		- cas opazovanja
		- smer in amplituda stopnice
	2. povezava potrebnih signalov na reg blok v blokovni shemi
		- tipko na celni plosci vezemo na signal za prozenje procesa samonastavljanja
		- na ustrezen vhod bloka za samonastavljanje povezemo izhod procesa
	3. rocno pripeljemo proces v zeljeno delovno tocko
	4. s tipko sprozimo samonastavitev

## Regulator SIPART DR24
- Večnamenski regulator
- Veliko število funkcijskih blokov
- Tipke in prikazovalniki na čelni plošči
- Modularna zgradba
	- standardna enota
	- razširitveni moduli
- Komunikacijske možnosti
	- RS232, SIPART BUS
	- RS485
	- PROFIBUS-DP
### Standardna enota
- __Zgrajena iz:__ 
	- osnovne plosce s CPU in prikljucnimi sponkami
	- celne plosce s tipkami in displayi
	- ohisja z razsiritvenimi porti
### Osnovna plosca
- zmogljiv mikrokrmilnik
- prilagodljiva I/O vezja
- pomnilnik

### Vhodno/izhodni signali
- 3 analogni vhodi
	- 0-1V
	- 0,2 - 1V
	- 0-10V
	- 2-10V
	- 4-20mA
- 3 analogni izhodi
	- 0-20 mA
	- 4-20 mA
- 8 binarnih izhodov
	- 0/24V
	- max obremenitev 50mA
- Pomozno napajanje 24V 100mA

### Razsiritveni moduli
- 3 dodatni analogni vhodi
	- uporovni senzor
	- temperaturni senzor Pt100
	- vhod za termoclen
- 3 dodatni analogni izhodi
	- en od njih je analogen z neodvisnim napajanjem in funkcijo hold
- Dodatni binarni izhodi
	- 2 relejska izhoda
	- modul s 4 binarnimi izhodi in 2 vhodoma
- Komunikacijski modul za RS232 / RS485 / PROFIBUS

### Funkcije

 

# Reference
# Tags
#template 