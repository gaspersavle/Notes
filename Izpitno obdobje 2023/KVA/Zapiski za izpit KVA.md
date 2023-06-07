### 1. Primer izpita
1. __Kaj je namen postopka ciklicnega kodiranja (CRC) in v katerem sloju TCP/IP slojnostnega modela se uporablja?__

_Odg:_ Namen ciklicnega kodiranja (CRC) je zaznavanje napak v prenosu podatkov. nahaja se v [[KVA pojmi-plonk#Podatkovno linijski sloj (Data Link)|Podatkovno linijskem sloju]] sloju[[iso_osi.png| ISO/OSI]] modela

2. __Z delilnim polinomom G(x) = x^3 + x^2 izvedite postopek CRC na podatkih 1101101 (ne pozabite dodati primernega stevila  nicel pri deljenju)__

_Odg:_ Navodila za rocno izvedbo CRC:

1. _KORAK:_ Na konec podatkov dodamo doloceno stevilo nicel _stevilo dodanih nicel je enako stevilu nicel delilnega polinoma minus 1_ oziroma racunsko:
$$N_{nicel} = N[stevilo \space od](G(x) = 0)$$
	V tem primeru ima delitelj 3 nicle, zato dodamo na konec podatkov _2 nicli_
	
2.  _KORAK:_ Delilni polinom zapisemo kot vsoto koeficientov vseh stopenj, torej: $$x^{3}+ x^{2}= (1 \cdot x^{3}+ 1 \cdot x^{2}+ 0 \cdot x + 0 \cdot 1)$$
	Ce je koeficient pred clenom enak 1, _bomo ta clen binarno predstavili z logicno " 1 "_, ce je koeficient pred clenom 0, pa _ta clen predstavimo z binarno " 0 "_. Delilni polinom se torej preoblikuje v __"1 1 0 0"__

Nato med podatkom in binarno predstavljenim delilnim polinomom _izvedemo operacijo XOR_, operacijo izvajamo _ciklicno_ , torej nad rezultatom vakega cikla znova izvedemo XOR. Pri tem delilnik v vsakem ciklu zamaknemo __do naslednje enice desno__.
 |1|1|0|1|1|0|1|_0_|_0_|
 |-|-|-|-|-|-|-|-|-|
 |1|1|0|0||||||
 |_0_|_0_|_0_|_1_|1|0|1|0|0|
 ||||1|1|0|0|
 |0|0|0|_0_|_0_|_0_|_1_|0|0|
 |||||||__1__|__0__|__0__|

Ko smo opravili z deljenjem (ko nam ostane manj znakov, kot je dolg delilnik), zmo dobili __ostanek deljenja__, sedaj ta ostanek _prelozimo na konec podatka_, torej dobimo:
1 1 0 1 1 0 1 _0 0_ __1 0 0__

4. _KORAK:_ Ostanek prejsnje operacije je rezultat crcja in _novi podatek, ki ga prenasamo_, na drugi strani se nad podatkom spet izvede operacija deljenja, _ce je ostanek 0, vemo da je podatek na cilj prispel nespremenjen_



3. __V sliki imate primer omrezja 3 vozlisc (V1, V2 in V3), ki so priklopljena na usmerjevalnikR. Omrezni naslovi vozlisc so oznaceni z IP, fizicni pa z E. Omrezje je ravno zacelo delovati in vozlisce V1 zeli poslati paket vozliscu V3. Vozlisca bodo uporabila protokol ARP
	1. _Kaj je vloga MAC in v cem se razlikuje po funkcionalnosti od naslova IP?_
		Odgovor: Vloga MAC naslova je, da se maprave na omrezju lahko prepoznajo na fizicnem nivoju, deluje na nivoju _lokalnega omrezja_, medtem ko se IP naslov uporablja za identifikacijo naprav na _internetu_, torej deluje na visjem, _omreznem nivoju_ (network layer)
		
	2.  _Zapisite po korakih postopek ARPa za sliko. Za vsak korak napisite katero vozlisce poslje paket in zapisite vsebino paketa s polji, ki so skicirana v sliki_
		
![[Pasted image 20230113131045.png]]
![[Pasted image 20230113131129.png]]
[[|ARP postopek]] __za sliko:__
- _V 1_ pregleda svoj cache, ce ima morda ze shranjen _MAC naslov_ prejemnika (V 3)
- Ce _V 1_ nima shranjenega _MAC_ naslova prejemnika, poslje broadcast paket  _ARP request_, ki vsebuje _MAC naslov posiljatelja_ in  _broadcast IP naslov_ 
	- _IP prejemnika:_ 255.255.255.255
	- _MAC posiljatelja:_ E 1 
| |MAC src| IP src| MAC dst|IP dst|opcode|
|-|-|-|-|-|-|
|_ARP_|E 1|IP 1||IP 3|1|

- _Vse naprave v omrezju prejmejo ARP request paket__

| |MAC src| IP src| MAC dst|IP dst|opcode|
|-|-|-|-|-|-|
|_ARP_|E 1|IP 1||IP 3|1|

- Na arp request se lahko _odzove samo naslovljena naprava_, torej se _V 3_ na request odzove in poslje _ARP reply_ paket, ki pride do _V 1_

| |MAC src| IP src| MAC dst|IP dst|opcode|
|-|-|-|-|-|-|
|_ARP_|_E 3_|IP 3|E 1|IP 1|2|



4.  __Po daljsem opazovanju komunikacijskega kanala smo ugotovili, da je verjetnost za enico enaka 2/10, verjetnost za niclo pa 8/10. Vasa naloga je sestaviti kod, ki kodira po dva zaporedna bita in  katerim boste optimalno kodirali binarna sporocila, ki se podrejajo zgornji statistiki. S tem kodom nato zakodirajte sporocilo 0000101000 in povejte koliko bitov (ce spoloh) prihranite ob kodiranju

_Odg:_

### 2. Primer izpita

1. __S postopkom CRC izrcunajte za sekvenco bitov 10101101101 razsirjeno binarno sekvenco, ki jo naprava, ki uporablja CRC, odda v komunikacijski kanal. Za delilni polinom uporabite
	G(x) = x^3 + x^2 + 1

_Odg:_

|1|0|1|0|1|1|0|1|1|0|1|_0_|_0_|
|-|-|-|-|-|-|-|-|-|-|-|-|-|
|1|1|0|1||||||||||
|_0_|_1_|_1_|_1_|1|1|0|1|1|0|1|0|0|
||1|1|0|1|||||||||
||_0_|_0_|_1_|_0_|1|0|1|1|0|1|0|0|
||||1|1|0|1|||||||
||||_0_|_1_|_1_|_1_|1|1|0|1|0|0|
|||||1|1|0|1||||||
|||||_0_|_0_|_1_|_0_|1|0|1|0|0|
|||||||1|1|0|1||||
|||||||_0_|_1_|_1_|_1_|1|0|0|
||||||||1|1|0|1|||
||||||||_0_|_0_|_1_|_0_|0|0|
||||||||||1|1|0|1|
||||||||||_0_|_1_|_0_|_1_|
|||||||||||__1__|__0__|__1__|

  2. __V sliki imate primer 2 naprav, N1 in N2, ki komunicirata prek TCP protokola. Naprava N1 poslje napravi N2 zaporedoma 2 TCP paketa s podatkovnim delom dolzine 1380 B. Naprava N2 odgovori s potrditvenim paketom, nato pa poslje svoj TCP paket s podatki dolzine 10 B. Na ta paket naprava N1 odgovori s potrditvenim pakeom. V sliki izpolnite manjkajoca polja:__ 
  - _Ack num (potrditvena stevilka)_
  - _Seq num (sekvencna stevilka)_

![[Pasted image 20230113132729.png]]
_Odg:_


3. __V sliki imate primer omrezja treh vozlisc (V1, V2 in V3), ki so priklopljeni na usmerjevalnik R. Omrezni naslovi so oznaceni z IP, fizicni pa z E. Omrezje je ravno zacelo delovati in vozlisce V1 zeli poslati paket vozliscu V3. Vozlisca bodo uporabila protokol ARP
	1. _Kateri specificen problem resuje protokol ARP?_
	2. _Zapisite po korakih postopek ARPa za sliko. Za vsak korak zapisite katero vozlisce poslje paket in zapisite vsebino paketa s polji, ki so skicirana v sliki_
![[Pasted image 20230113133248.png]]

_Odg:_
- _V 1_ pregleda svoj cache, ce ima morda ze shranjen _MAC naslov_ prejemnika (V 3)
- Ce _V 1_ nima shranjenega _MAC_ naslova prejemnika, poslje broadcast paket  _ARP request_, ki vsebuje _MAC naslov posiljatelja_ in  _broadcast IP naslov_ 
	- _IP prejemnika:_ 255.255.255.255
	- _MAC posiljatelja:_ E 1 
| |MAC src| IP src| MAC dst|IP dst|opcode|
|-|-|-|-|-|-|
|_ARP_|E 1|IP 1||IP 3|1|

- Vse naprave v omrezju, _vkljucno z usmernikom_ prejmejo ARP request paket, vendar vse to poteka prek usmernika, torej _usmernik prestreze paket_

| |MAC src| IP src| MAC dst|IP dst|opcode|
|-|-|-|-|-|-|
|_ARP_|E 1|IP 1||IP 3|1|

- _Usmernik pregleda svoj cache_, ce ima ze shranjen MAC prejemnika, ce ga nima, _posreduje ARP request vsem napravam na mrezi_

| |MAC src| IP src| MAC dst|IP dst|opcode|
|-|-|-|-|-|-|
|_ARP_|E rb|IP rb||IP 3|1|


- Na arp request se lahko _odzove samo naslovljena naprava_, torej se _V 3_ na request odzove in poslje _ARP reply_ paket, ki pride do _usmernika_

| |MAC src| IP src| MAC dst|IP dst|opcode|
|-|-|-|-|-|-|
|_ARP_|E 3|IP 3|E rb|IP rb|2|


- _Usmernik_ iz paketa nalozi _MAC naslov naprave V 3 v svoj cache_ in ga nato v novem ARP reply paketu posreduje _originalnemu posiljatelju V 1_

| |MAC src| IP src| MAC dst|IP dst|opcode|
|-|-|-|-|-|-|
|_ARP_|_E 3_|IP 3|E 1|IP 1|2|



4.  __Kaj je namen protokola DHCP? recimo, da se priklopite med vasim racunalnikom v novo omrezje, v katerem se nahaja naprava s stevilko IP = 192.168.1.1, na kateri tece DHCP streznik. Vas racunalnik pa pricne s postopkom protokola DHCP
	1. _Zapisite sekvenco paketov, ki se posljejo med vasim racunalnikom in DHCP streznikom. Za vsak paket napisite cemu sluzi, prav tako pa za vsak paket izpisite tudi njegove izvorne in ponorne stevilke IP_
		1. nas racunalnik poslje _DHCP discover_, izvorni naslov paketa je nas naslov, ponorni pa je _broadcast_
		2. Streznik na naslovu 192.168.1.1 prejme naso zahtevo in nanjo odgovori z _DHCP offer_, ta ponudba vsebuje IP naslov, ki ga bo nas racunalnik lahko uporabljal, masko podomrezja, privzeti gateway in DNS streznik. Izvorni naslov paketa je 192.168.1.1, ponorni naslov pa je naslov nasega racunalnika
		3. Nas racunalnik poslje _DHCP request_, ta paket vsebuje izvorni IP naslov, ki se je spremenil v tega, ki nam ga je _v prejsnjem koraku delegiral streznik_, ponorni naslov pa je naslov streznika (192.168.1.1), s tem __potrdi izbiro novega naslova__
		4. Streznik na request odgovori s paketom _DHCP ACK_, ponorni naslov je nas novo - delegirani naslov, izvorni pa je naslov streznika. S tem je server odobril naso uporabo novega IP naslova. DHCP strezniik _hrani novo delegirani IP naslov_

	2. _Cemu sluzi znacka "transaction ID" v DHCP paketih? Napisite primer mozne problematicne situacije, ki bi nastopila, ce te znacke ne bi bilo v protokolu_
		- Transaction ID (znana tudi kot xID) je identifikacija transakcije, ki _se uporablja za sinhronizacijo med DHCP streznikom in odjemalcem_. Odjemalec in streznik si delita isti xID, kar omogoca odjemalcu, da prepozna katere pakete je prejel od streznika in jih lahko _ustrezno obdela_.
	3. _Kaj pomeni znacka "Lease time"?_
		-  Lease time nam sporoca _casovni interval, ko nam je dovoljeno uporabljati isti IP naslov_, saj nam jih DHCP streznik dodeli le za dolocen cas. Ko pretece lease time odjemalec zgubi uporabo tega naslova in se mora ponovno povezati na streznik, ki mu dodeli nov naslov IP.

_Odg:_

#kva #zapiski #isoOsi #izpit 