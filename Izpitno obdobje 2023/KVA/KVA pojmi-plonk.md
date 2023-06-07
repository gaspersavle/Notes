# Osnovne oblike tehnologije
Razlikujejo se po nacinu dostopa do prenosnega sredstava oziroma medija
- Zvezda:
	- Pozivanje, 
	- Izbiranje
![[Pasted image 20230121160051.png]]
- Obroc
	- Zeton (token)
![[Pasted image 20230121160128.png]]
- Vodilo (bus)
	- Zeton (token)
	- Nakljucen dostop
![[Pasted image 20230121160151.png]]

# ISO-OSI model
![[ISO-OSI.png]]
## Fizicni sloj (Physical)
- Skrbi za prenos digitalnih signalov po prenosnih linijah (katerakoli oprema: ethernet, coax,...)
- _Osnovna podatkovna enota je_ __BIT__
## Podatkovno linijski sloj (Data  Link)
- Sktbi za kar se da zanesljiv prenos okvirjev med sosednjimi vozlisci. 
- _Osnovna podatkovna enota je_ __OKVIR__ _(zaporedje bitov)_
## Omrezni sloj (Network)
- Zagotavlja prenosne poti med poljubnima vozliscema (nodes), ki sta lahko tudi v razlicnih omrezjih.
## Prenosni sloj (Transport)
- Skrbi za prenos podatkovnih enot skozi omrezje od izvornega do ponornega vozlisca
- _OSnovna podatkovna enota je_ __SEGMENT__
- [[#TCP]]
- [[#UDP]]
## Pogovorni sloj (Session)
- Skrbi za prenos podatkovnih enot skozi omrezje od izvornega do ponornega __PROCESA__
- Tako izvorno, kot ponorno vozlisce vsebujeta vec _procesov_
- _Osnovna podatkovna enota je_ __PROTOKOLOVNA PODATKOVNA ENOTA ali PDU__
## Predstavitveni sloj (Presentation)
- Skrbi za:
	- Ustrezno kodiranje in prekodiranje podatkov
	- Zgoscevanje podatkov
	- Sifriranje podatkov
- _Osnovna podatkovna enota je_ __BLOK PODATKOV__
## Aplikacijski sloj
- Skrbi za zagotavljanje storitev koncnemu uporabniku omrezja
- Upravlja z:
	- Elektronsko posto
	- Prenosom datotek
	- WWW (svetovni splet)
	- SMTP (simple mail transfer protocol)
	- FTP (file transfer protocol)
	- HTTP (hypertext transfer protocol)
	- MMS (multimedia messaging service)
	- OPC (open platform communications)
- _Osnovna podatkovna enota je_ __SPOROCILO__

# CSMA / CD
- Carrier Sense Multiple Acces / Collision Detection
- Oziroma _poslusaj tudi, ko govoris_
	- Ce kanal ni prosti _pocakaj z oddajo_
	- Ce je kanal prost _zacni z oddajo_
	- Ce trcis _prekini oddajo in poskusi ponovno po nakljucnem casu_
- Razlika med tem protokolom in _CSMA_ je, da se v primeru SMA/CD v primeru trcenja oddaja _ne nadaljuje_
- Ker se pri uporabi _CSMA/CD_ prej sprosti vodilo, pricakujemo boljsi izkoristek prenosa podatkov
- _Izkoristek prenosa:_ $$E_{CSMA-CD}= \frac{1}{1+3\cdot\frac{\tau}{T_f}} $$
- Kjer _T_ pomeni [[#Krmilni cas omrezja]], _T_f_ pa pomeni [[#Cas trajanja okvirja]], stevilka _3_ pa predstavlja [[#Stevilka optimalnega bremena| stevilko optimalnega bremena]].

### Dostop do prenosnega sredstva v omrezju CSMA / CD
- _CSMA/CD_ realizira nakljucen dostop do kanala. To pomeni, da ne moremo zagotovo napovedati kdaj bo oddajnik prisel na vrsto. ^136320
- V primeru trka se oddaja prekine in ponovno poskusi _po nakljcnem casu_


# TCP
- Transmission Control Protocol
- Omogoca povezano, zanesljivo, sekvencno storitev, _brez podvajanja ali izgube paketov_
- TCP segment _se prenese v enem ali vec IP paketih_ 
- Uporablja se za prenos podatkov, ki zahteva visoko zanesljivost in strikten vrstni red paketov.
- Podatki potujejo v vrstnem redu v katerem so bili poslani

__IP datagram:__
| IP glava | TCP glava | TCP podatki |
|-|-|-|
|20 Bajtov | 20 Bajtov | 
\                  _^------------TCP segment----^_
\ ^-------------------------- IP datagram-----^

## TCP glava
![[Pasted image 20230119133217.png]]
- __Velikost je vsaj 20 bajtov__
- _Source port:_ Identifikacija izvornih vrat
- _Destination port:_ Identifikacija ponornih vrat
- _Sequence number:_ Vrstna stevilka paketa, igra dvojno vlogo:
	- Ce je [[#zastavica SYN]] postavljena na 1  je to _zacetna sekvencna stevilka_, ki bo povecana za 1 postala _zacetna potrditvena stevilka_ ([[#^15dc56|acknowledgment number / AckNo]])
	- Ce je  [[#zastavica SYN]]  postavljena na 0, je to _akumulirana sekvencna stevilka_ prvega bajta trenutnega segmenta
- _Acknowledgment number:_ Potrditvena stevilka paketa ^15dc56
	- Ce je [[#zastavica ACK]] postavljena, bo vrednost tega polja postalo _naslednja sekvencna stevilka_, ki jo bo posiljatelj [[#^e4dbd4| ACK paketa]] pricakoval.
	- To _potrdi prejem vseh bajtov pred tem_
	- Prva ACK stevilka, ki ga poslje vsaka stran prenosa, bo postala prva sekvencna stevilka nasprotne strani
- _Data offset:_ Specificira velikost TCP glave v _32 bitnih besedah_ (torej oznaka 1101 pomeni, da je glava dolga 13 32-bitnih besed)
	- Minimalna velikost glave je 5 besed, maksimum pa 15
	- Ime izvira iz tega, da _ta dolzina pomeni zamik dejanskega podatka od zacetka  TCP segmenta_
- _Zastavice:_ 
	- _NS (nonce sum):_ signalizira, da segment vsebuje podatek "nonce", ki se uporablja za preprecevanje napadov s ponavljanjem. Zastavica pove prejemniku, da mora preverjati ta podatek
	- _CWR (Congestion Window Reduced):_ Zastavico postavi posiljatelj in signalizira, da je prejel TCP segment z zastavico [[#^68c81f|ECE]]
	- _ECE (Explicit Congestion Notification Echo):_ Se uporablja za javno obvestilo o nasicenju prenosne poti. Omogoca posrednikom, da _javno sporocijo klientu, da se na njihovem podrocju dogaja zamasitev_. 
		- _Zastavica torej signalizira, da posrednik, ki jo posreduje sporoca klientu zamasitev_^68c81f
	- _URG (Urgent):_ Signalizira, da so podatki, ki se posiljajo v tem paketu _nujno pomembni in morajo biti prednostno prejeti_
		- Uporablja se naprimer za prekinitvene signale ali podatke o napakah
		- Uporablja se skupaj s poljem "URGENT POINTER", ki oznacuje kateri bajt v segmentu je nujen
	- _ACK (Acknowledge):_ Pomeni, da je polje pomembno, vsi segmenti po izvirnem [[#^6b6267|SYN paketu]] bi morali imeti to zastavico postavljeno na 1
	- _PSH (Push):_ Zahteva, da se poslani podatki direktno preslikani aplikacijskemu nivoju
	- _SYN (Synchrnise SeqNo):_ Samo prvi paket, poslan s klienta in streznika bi moral imeti to zastavico postavljeno. Nekatere ostale zastavice spremenijo funkcije glede na stanje zastavice SYN
	- _FIN (Zadnji paket):_ Signalizira, da je posiljatelj poslal vse podatke in da obe strani prenosa lahko zacneta s procesom terminacije komunikacije.
## Vzpostavitev zveze
Uporabljamo [[#Trikratno usklajevanje]] oziroma three way handshake

- Ko se poslje paket _SYN_ zacne z neko sekvencno stevilko _SeqNo_
- Ko ta paket prejme streznik, generira svojo sekvencno stvilko, ter za _potrditveno stevilko AckNo_ pristeje 1 sekvencni stevilki _prejetega paketa_, temu "odgovoru" na paket odjemalca pravimo Sync- acknowledge, oziroma _SYN-ACK_
- Ko odjemalec prejme _SYN-ACK_ paket, nanj odgovori s paketom _ACK_ v katerem za _SeqNo_ povisa svojo originalno za 1, ter za _AckNo_ uporabi za 1 povecan _SeqNo_ prejetega _SYN-ACK_ paketa
![[Pasted image 20230121155007.png]]
## Vzdrzevanje zveze
![[Pasted image 20230121155207.png]]
- Zaradi podatka "HALO" se AckNo v primeru druge puscice zamakne za 4 bajte, _ker je vsak ASCII znak velik 1 bajt, sporocilo pa je dolgo 4 bajte_

## Maxinum segment size (MSS)
- [[#TCP glava]] ne vsebuje polja, ki bi pomenilo dolzino segmenta, _Maximum Segment Size je parameter samega protokola ali omrezja_
- 
# UDP
- User Datagram Protocol
- Omogoca nepovezano, nezanesljivo storitev v kateri je mozno podvajanje ali izgubljanje paketov _za ceno hitrosti in REAL TIME delovanja_
- Vsak UDP paket se prenasa v svojem IP paketu, _da se izognemo fragmentaciji_.
- Ko oddajnik dobi podatke od aplikacije, na podatke doda glavo in ta _datagran_ takoj posreduje [[#Omrezni sloj (Network)|omreznemu sloju]] ter nanj pozabi.
- Podatki se posredujejo kot so, torej se ne preverja njihovega vrstnega reda ali pravilnosti. Aplikacijskemu sloju prepustimo, naj se ukvarja z njimi.

__IP datagram:__
| IP glava | UDP glava | UDP podatki |
|-|-|-|
|20 Bajtov | 8 Bajtov | 
\                  _^------------UDP datagram--^_
\ ^-------------------------- IP datagram-----^

- _UDP glavo_ sestavljata stevilki vrat izvora in ponora
- Sprejemnik zavrze datagram, ce se checksum ne ujema


# ALOHA protokol
- ALOHA protokol je bil razvit za uporabo v radijskih omrežjih
- prvi omrežni sistem, ki je omogočil prenos podatkov med računalniki preko radijskega valovanja
- Glavna značilnost ALOHA protokola je, da vsak računalnik poskuša poslati podatke hkrati, ne da bi se dogovarjal za čas prenosa. Če več računalnikov poskuša poslati podatke hkrati, lahko pride do _trcenja_, kjer se podatki med seboj prekrijejo in ne morejo biti prebrani.
- ALOHA protokol uporablja metodo za reševanje trcenj, ki se imenuje Pure ALOHA. Ta metoda pomeni, da _vsak računalnik pošlje podatke takoj, ko so na voljo_, in če pride do trcenja, vsi računalniki, ki so bili vključeni, dolocijo naključen časovni interval in poskusijo ponovno poslati podatke
- _Preprostost in hitrost hitro padeta z obremenitvijo omrezja_
- __Ucinkovitost ALOHA:__$$E_{ALOHA} = \frac{P_{1OPT} \cdot T_{f}}{2\cdot T_{f}}$$$$P_{k}= \frac{ \lambda^{k}\cdot e^{- \lambda}}{k!} $$
$$P_{1}= (2\lambda)\cdot e^{-2 \lambda}$$
$$P_{1OPT} = e^{-1}$$
- Kjer je:
	- $k$ - _Sekvencna stevilka okvirja_ 
	- $\lambda$ - _Povprecno strevilo oddaj na okvir_

# ARP protokol
- Omogoča računalnikom v lokalnem omrežju, da določijo fizične naslove (MAC) drugih računalnikov, ki so povezani v to omrežje z uporabo njihovih IP naslovov.
- Vsak računalnik v omrežju hrani _ARP tabelo_, v kateri so shranjeni _pari IP naslova in ustreznega MAC naslova_
- Ko računalnik želi poslati podatke drugemu računalniku, ki je na istem omrežju, _preveri svojo ARP tabelo_
- Če ni zabeleženega ustreznega MAC naslova, pošlje _ARP zahtevo_ v omrežje (BROADCAST)
- Ciljni računalnik, ki ima ustrezni IP naslov, _odgovori s svojim MAC naslovom_
- Prednost uporabe ARP protokola je, da _omogoča računalnikom, da se medsebojno komunicirajo brez potrebe po imenikih ali drugih vrstah spremljanja_
- Pomanjkljivost je, da so ARP zahteve lahko zlorabljene za napade na omrežja in da ARP tabela ni zaščitena pred spreminjanjem

# MAC naslov
- MAC naslov (Media Access Control address) je _unikatna šestnajstiška oznaka_, ki je določena v vsaki mrezni kartici in je uporabljena za identifikacijo naprave na [[#Podatkovno linijski sloj (Data Link)|povezovalnem nivoju]]

# IP naslov
- IP naslov (Internet Protocol address) je _binarna oznaka, ki se uporablja za identifikacijo računalnika ali naprave na internetu_.

## Razlike med MAC in IP naslovom
-   MAC naslovi so _unikatni za vsako napravo_ in jih ni mogoče spremeniti. IP naslovi pa se lahko spremenijo.
-   MAC naslovi so _omejeni na nivo omrežja_, medtem ko se IP naslovi uporabljajo za komunikacijo _na internetnem nivoju_.
-   MAC naslovi se uporabljajo za dostop do omrežnega medija, medtem ko IP naslovi se uporabljajo za prenos podatkov prek omrežja.

# IP PAKET
- IP paket (Internet Protocol packet) je enota podatkov, ki se uporablja za _prenos podatkov prek interneta_ in drugih omrežij, ki uporabljajo IP protokol
- Podatkovni del IP paketa vsebuje podatke, ki se prenašajo. Kot so npr. datoteka, sporočilo...
- IP paketi se lahko prenašajo prek različnih omrežnih naprav, kot so _usmerniki_, vsak usmernik pregleduje glavo IP paketa, da določi, kam naj ga pošlje dalje. Ta proces se imenuje "_usmerjanje_" in omogoča prenos podatkov med računalniki, ki se nahajajo na različnih omrezjih.
## IP glava
- Glava IP paketa vključuje informacije o naslovih, ki se uporabljajo za prenos podatkov, kot so naslov prejemnika in naslov pošiljatelja ter kontrolne informacije, kot so [[#identifikator paketa]], [[#Zastavice]] in drugo.

![[Pasted image 20230119004950.png]]

### Zastavice (Flags)
- Zastavice IP paketa (ang. IP packet flags) so skupina bitov v glavi IP paketa, ki _se uporabljajo za kontroliranje različnih lastnosti prenosa podatkov_. Glavne zastavice IP paketa so:
	-  _DF (Don't Fragment):_ To zastavico lahko nastavi pošiljatelj paketa in _označuje, da se paket ne sme razbijati_, če se zgodi, da je večji od dovoljene velikosti za določeno omrežno napravo. V tem primeru bo usmernik paket zavrgel.
    
	-  _MF (More Fragments):_ To zastavico lahko nastavi posrednik in _označuje, da sledijo še drugi fragmenti IP paketa_, ki jih je treba prejeti za popolno prejemanje podatkov.
   ^aa24a9   ^d1102f
	-  _RF (Reserved fragment):_ To zastavico se uporablja za rezerviran fragment, ki se ne uporablja.
    
	-  _offset:_ ta zastavica označuje položaj fragmenta v izvornem paketu.

### Identifikator paketa (Packet ID)
- Stevilčna oznaka, ki se uporablja za identifikacijo posameznih paketov med prenosom podatkov prek omrežja.
- To polje doloci posiljatelj
- Se uporablja za prepoznavanje paketov med prenosom, saj lahko različni paketi potujejo skozi iste omrežne naprave in se prepletajo

### Time to live (TTL)
- TTL (Time to Live) je polje v glavi IP paketa, ki _se uporablja za omejevanje števila posrednikov, preko katerih lahko paket potuje na svoji poti do cilja._
- inicializira se na določeno število (običajno 64, 128 ali 255) pri pošiljanju paketa in se _vsakič, ko paket potuje skozi usmernik ali kakrsnokoli drugo napravo na njegovi poti, zmanjša za 1_. Ko TTL doseže 0, se paket zavrne in pošlje se sporočilo o napaki "TTL expired" nazaj pošiljatelju.
- Uporablja se za preprečevanje zanke v omrežju, kjer bi lahko paket neustavljivo potoval skozi omrežje, ker ni dosegel cilja. To lahko povzroči preobremenjenost omrežja in zmanjšanje učinkovitosti.

## Fragmentacija in sestavljanje
- Omrezja imajo navzgor omejeno velikost prenosljive podatkovne enote
- Vecji IP datagrami se zato _delijo ali fragmentirajo_, iz enega datagrama nastane vec datagramov, oziroma _fragmentov originalnega datagrama_.
- V IP glavi imajo vsi fragmenti enako oznako, razlicno zaporedno stevilko in _zastavico_, ki signalizira:
	- Da je to vmesni fragment: [[#^aa24a9|Zastavica MF (More Fragments) = 1]]
	- Da je to zadnji fragment: [[#^d1102f|Zastavica MF (More Fragments) = 0]]
- Fragmenti se znova sestavijo sele  v zadnjem, ponornem vozliscu. Usmerniki se ne ukvarjajo s tem
- __Primer fragmentacije in sestavljanja:__
![[Pasted image 20230120223802.png]]
# DHCP
- Je protokol, ki _omogoča avtomatsko konfiguracijo IP naslovov za naprave na omrežju_. DHCP server deluje kot centralni vir konfiguracijskih podatkov
- Naprave (klienti) _pošljejo zahteve za konfiguracijo_, ki jih server posreduje.
- DHCP _omogoča dinamično spremembo IP naslova naprave_, če je potreben, kar pomeni, da lahko naprava pridobi nov IP naslov, če se stari naslov izgubi ali je potreben za druge naprave.

| Lease time | Dolzina polja (4 B) | Poljubno lease time v sekundah (4 B)|
|-|-|-|

## Vzpostavitev povezave z DHCP
Vzpostavitev poteka prek 4 korakov

1.  _DHCP zahteva (DHCP discover)_: Naprava (klient) _pošlje broadcast zahtevo za DHCP server_, zahteva vsebuje posiljateljev MAC naslov in zahteva nov IP naslov.
    
2. _DHCP ponudba (DHCP offer):_ ko DHCP server prejme zahtevo, _pošlje ponudbo za IP naslov klientu_, ki vsebuje:
	- klientov MAC naslov, 
	- predlagan naslov IP, 
	- masko podomrezja,
	- trajanje IP naslova
	- IP naslov DHCP streznika
    
3. _DHCP zahteva (DHCP request):_ Je odgovor klienta na DHCP ponudbo, v kateri _klient zahteva ponujeni IP naslov_, saj lahko dobi ponudbo z vecih DHCP streznikov. Paket vsebuje:
	- Identifikacijo izbranega streznika
	- Svoj nov IP naslov
	- Svoj MAC naslov
    
4.  _DHCP aktivacija: (DHCP acknowledge)_ DHCP server potrdi, da je klient aktiviral konfiguracijske podatke in povezava je vzpostavljena. Paket vsebuje:
	- Trajanje IP naslova
	- Konfiguracijske podatke, ki jih je zahteval odjemalec

| 1 _(C->S)_| DISCOVER| 
| -| -|
|2 __(S->C)__ | OFFER|
|3 _(C->S)_|REQUEST|
| 4 __(S->C)__ | ACKNOWLEDGE|

## Transaction ID
- Stevilka, ki se uporablja zaprepoznavo DHCP transakcije med odjemalcem in streznikom.
- _Omogoca klientu in strezniku, da ugotovita na katero zahtevo se nanasa kateri odziv_ in prepreci zmedo med vecjo kolicino DHCP transakcij, ki se izvajajo hkrati.

# ICMP 
Je podporni/nadzorni protokol _IP protopkolu_
- Deluje na [[#Omrezni sloj (Network)| omreznem sloju]]
- ICMP glava je _enaka_ [[#IP glava|IP glavi]]
Uporablja se za:
- Sporocanje napak med napravami
- Nadzor zasicenosti omrezij
- Preizkusanje dosegljivosti vozlisc
- Preusmerjanje
- Merjenje zmogljivosti
- Podomrezno naslavljanje

ICMP sporocilo je lahko _poizvedba, odgovor ali napaka_
[[#Traceroute]] je program, ki pomaga izslediti pot do oddaljenega koncnega vozlisca. 

# NAT
Network adress translation
- Omogoca _napravam na zasebnem omrezju, da komunicira jo z napravami na javnem omrezju_ z uporabo _edinstvenega javnega IP naslova_
- _Mapira zasebne IP naslove naprav na omrezju na en javni IP naslov_, ki se uporablja za komunikacijo z napravami na javnem omrezju
- To omooca, da _vec naprav na istem omrezju uporablja isti IP naslov_, kar varcuje z omejenim stevilom IPV4 naslovov.
- Mapiranje med zasebnimi in privatnimi IP naslovi _hrani NAT usmerjevalnik v NAT tabeli_

__Potreba za NAT:__
- Razsiritev naslovnega prostora
- Vecja fleksibilnost pri _dodeljevanju naslovov_
	- Notranje naslove s elahko svobodno dodeljuje
	- Notranji naslovi lahko ostanejo nespremenjeni, tudi ce zamenjamo operaterja
- Varnost: Notranji naslovi navzven niso vidni, kar poveca varnost

# DNS
Domain Name System
- Sistem, ki _prevaja imena domen v IP naslove_.
- Namenjen je za _lajsanje dostopa do spletnih strani in drugih internetnih storitev za uporabnike
- DNS omrezje je _hierarhicno in decentralizirano_, kar pomeni, da so podatki o imenih domen in ip naslovih _razporejeni po razlicnih streznikih po vsem svetu_
- Ko uporabnik poslje zahtevo za dostop do streznika, _njegov racunalnik poisce ustrezen streznik DNS_, ki ima podatke o tem _kateri naslovi se navezujejo na dolocene domene_
- Omogoca enostaven in intuitiven dostop do spleta brez potrebe po pomnjenju IP naslovov



# Razlaga pojmov
## Krmilni cas omrezja
Krmilni čas omrežja je čas, ki je potreben za izvedbo kontrolnih dejavnosti v omrežju. To lahko vključuje dejavnosti, kot so:
- usklajevanje, 
- sinhronizacija, 
- pregled stanja,
- upravljanje kapacitete,
- spremljanje napak 

Krmilni čas omrežja se lahko razlikuje glede na različne protokole in konfiguracije omrežja. Cilj je zagotavljanje optimalnega delovanja omrežja, in zmanjševanje časa odziva in zastojev.

## Cas trajanja okvirja
Čas trajanja okvirja, pogosto imenovan tudi "čas okvirja", je _čas, ki je potreben za prenos okvirja (paketa) med dvema točkama v omrežju_. To vključuje čas, ki je potreben za prenos podatkov okvirja skozi vse sloje omrežja, vključno z fizičnim slojem (za prenos bitov) in omrežnim slojem (za prenos paketov) ter za procesiranje podatkov na vsakem koraku.
Čas trajanja okvirja se lahko spreminja glede na različne dejavnike, kot so hitrost prenosa, stanje omrežja, velikost okvirja in obremenjenost omrežja.

## Stevilka optimalnega bremena
Kot optimalno breme we uporablja stevilka "_L_", ki _predstavlja dolžino okvirja v bitih_. Optimalno breme se uporablja za določene primere, ko je učinkovitost omrežja najvišja prioriteta. _Prekratki okvirji lahko povzročijo preveliko obremenitev omrežja_, medtem ko _predolgi okvirji lahko povzročijo preveliko zakasnitev_. Torej _L je dolžina okvira, ki omogoča optimalno izkoriščenje omrežja._

## Trikratno usklajevanje
  
Trikratno usklajevanje (angl. three-way handshake) je proces, ki se uporablja pri protokolu TCP za vzpostavitev povezave med dvema računalnikoma. Trikratno usklajevanje sestoji iz naslednjih treh korakov:

1.  _SYN_ (Synchronize) paket: Prvi računalnik pošlje paket SYN na drugi računalnik, ki ga označi kot zahtevo za vzpostavitev povezave.
     ^6b6267
2.  _SYN-ACK_ (Synchronize-Acknowledgment) paket: Drugi računalnik pošlje nazaj paket SYN-ACK, ki označuje, da je sprejel zahtevo za povezavo in da je pripravljen začeti prenos podatkov.
    
3.  _ACK_ (Acknowledgment) paket: Prvi računalnik pošlje paket ACK, ki označuje, da je prejel paket SYN-ACK in da je povezava uspešno vzpostavljena.
     ^b49d4e
Trikratno usklajevanje se uporablja za zagotavljanje, da oba računalnika vesta, da so se uspešno povezali in da lahko zacneta s prenosom podatkov. Ta proces se uporablja tudi za preklic povezave, ko se odstrani ACK paket. ^e4dbd4

## Traceroute
Programsko orodje, ki _omogoca pregled poti, po kateri paketi potujejo_ med posiljateljem in prejemnikom. Orodje deluje tako, da posilja pakete s cedalje vecjim [[#Time to live (TTL)]] in spremlja kateri posredniki jih prejemejo in vracajo [[#ICMP]] napako "TTL exceeded"

Razlogi za uporabo:
- _Diagnostika:_ Pregled poti omogoca administratorjem diagnostiko tezav, kjer se paketi izgubljajo ali kjer se pojavljajo zastoji na dolocenih posrednikih
- _Analiza:_ Traceroute omogoca pregled omrezne topologije, tako da lahko vidimo kateri posredniki so vkljuceni v prenos in kako so povezani med seboj
- _Analiza zasebnosti:_ Pri vpogledu v topologijo lahko vidimo, ce so pri prenosu udelezeni neznani posredniki ali posredniki v drugih drzavah, kar lahko nakazuje na zlorabe.

## Piggybacking
Tehnika dvosmerne komunikacije na [[#Omrezni sloj (Network)| omreznem sloju]], kjer podatke posiljamo prek ACK paketov

## Round trip time (RTT)
__EstimatedRTT:__ $$(new) \space estimatedRTT = (1- \alpha)\cdot estimatedRTT + \alpha \cdot sampleRTT$$$$(new) \space DevRTT = (1- \beta)\cdot DevRTT + \beta \cdot |estimatedRTT - sampleRTT|$$
$$TCP \space Timeout = estimatedRTT + (4\cdot DevRTT)$$


#kva #zapiski #isoOsi #izpit 