
04.01.2023
11:24
[[# Tags]]
[[# Reference]]

# Teme

## Pomen umetnega govora v inteligentnih sistemih
- naj bi se ne le zavedali prisotnosti ljudi, temvec _z njimi tudi komunicirali_
- govor je cloveku najnaravnejsi nacin komunikacije
- eden od ciljev inteligentnih sistemov je podpora cloveku naravne komunikacije s strojem
- v nadaljevanju bomo spoznali zasnovo sistema za tvorjenje umetnega govora iz poljubnega vhodnega besedila (sintetizator govora)

## Osnove tvorjenja govora
- za razumevanje postopkov tvorjenja umetnega govora je kljucno poznavanje osnov tvorbe govora _pri cloveku_
- prehod zraka skozi grlo ali nos, da zvoku poseben _zven_, ki je odvisen od oblike prostora skozi katerega prihaja
- glasovom, ki jih tvorimo z glasilkami pravimo _zveneci glasovi_
- ko zvoki ne zatresejo glasilk, ustvarjamo z jezikom v ustni votlini nekaksne turbulence, ki oblikujejo _zvocno sumenje_
- tem glasovom, ki jih tvorimo brez tresenja glasilk pravimo __nezveneci glasovi__

## Govorila
- cloveski organi, ki sodelujejo pri tvorbi govora
- __vkljucujejo:__
	- trebusno prepono
	- pljuca
	- sapnik
	- grlo
		- glasilki
		- poklopec
	- zrelna votlina
	- ustna votlina
		- strop
			- zgornji zobje
			- trdo nebo
			- mehko nebo
			- jezicek
		- ustnice
		- zobje
		- zgornja in spodnja celjust
		- jezik
	- nos

## Frekvencne znacilnosti govora in sluha
- obmocje slisnosti je odvisno od frekvence in glasnosti
	- vodoravno crtkano na grafu predstavlja obmocje govornega signala
	- navpicno crtkano na grafou predstavlja obmocje glasbe
- sposobnost zaznavanja sprememb v zvoku je nekje med 5 in 20 ms
- sposobnost zaznavanja razlik se s frekvenco spreminja
- minimalen cas za opredelitev signala je med 50 in 200 ms
- uho ni fazno obcutljivo
![[graf_slusne_obcutljivosti.png]]

## Znacilnosti zvocnega govornega signala
- _Caspvno spremenljiv_ nakljucni signal, casovna spremenljivost je posledica razlicnoih glasov, ki sestavljajo govor
- Na dovolj kratkih izsekih ga lahko obravnavamo kot stacionarni nakljucni signak
- Formanti so resonancne frekvence govornega trakta pri izreki dolocenega glasu
![[formantne_frekvence.png]]

## Porazdelitev formantnih frekvenc
- samoglasniki imajo izrazite resonancne frekvence
- prvi dve formantni frekvenci _F1 in F2_ se pogosto predstavlja na dvorazsezni F1/F2 ravnini
![[f1f2_ravnina.png]]

## Govorni glasovi in njihove znacilnosti
- Simbole za razlicne govorne glasove v nekem jeziku, s katerimi je mozno lociti posamezne besede jezika imenujemo fonemi (30-50 glasov)
- Pri opisovanju govora igrajo fonemi podobno vlogo kot pri pisavi _crke_
- Simbole za razlicne akusticne realizacije fonemov imenujemo _alofoni_
- _Fon_ imenujemo posamezno akusticno uresnicitev (izgovorjavo) glasu
- V slovenscini vse tri razlicne kategorije navadno poimenujemo kar z besedo _glas_

## Razvrscanje fonemov
1. Glede na nacin vzbujanja vokalnega trakta
	- Zveneci
	- Nezveneci
2. Glede na odprtost vokalnega trakta
	- Samoglasniki
	- Soglasniki
3.  Glede na nacin tvorjenja zvonikov
	- Zaporniki
	- priporniki
	- zlitniki
4. Glede na razclenitevposameznih faz tvorjenja zapornikov
	- Zapora
	- Odpora
	- Pridih
5. Glede na trajnost glasov
	- Trajni
	- Netrajni
6. Glede na uporabo dela vokalnega trakta
	- Ustni
	- Nosni

## Alofoni slovenskega govora
![[slovenski_alofoni.png]]

## Postopki tvorjenja umetnega govornega signala
- Raziskovalci so v zadnjih desetletjih razvili vrsto postopkov za tvorjenje umetnega govornega signala
- _Artikulatorni_ sintetizatorji govora so fizikalni modeli, ki so zasnovani na podlagi natancnega modeliranja fiziologije in akustike govornega trakta 
- So najstarejsi sintetizatorji govora, pbstajajo pa tudi novejsi poskusi zasnove mehanskih modelov
- _Formantni sintetizatorji_ govora predpostavljajo, da je prenosna funkcija govornega trakta zadovoljivo opisana s formantnimi frekvencami in formantnimi amplitudami
- Sinteza temelji na umeni rekonstrukciji formantnih znacilnosti
- Govor tvorijo s casovnim spreminjanjem _osnovnih govornih frekvencnih parametrov_, kot so predvsem formantne frekvence in tudi osnovni ton govora ter amplituda suma ipd.
- Navadno so izvedeni z mnozico produkcijskih pravil, na osnovi katerih se tvori umetni zvosni govorni signal

## Sintetizatorji govora z zdruzevanjem osnovnih enot
- Temeljijo na obdelavi vnaprej posnetih in natancno oznacenih, razclenjenih posnetkov naravnega govora
- Zbirke osnovnih enot mora biti sestavljena tako, da odraza _finoloske znacilnosti_ danega jezika
- Navadno se kot primerne osnovne enote obravnava difone, ki predstavljajo prehode med zaporednimi glasovi
- Sintetizator govora ob zdruzevanju govornih enot uporablja postopke obdelave signalov, da zgladi spektralne nezveznosti, ki nastanejo na zlepkih in hkrati nastavi zahtevane prozodicne parametre

### Postopki zdruzevanja osnovnih enot
- Za zdruzevanje osnovnih enot se med drugim lahko uporabi postopke obdelave signalov, ki temeljijo na vec pulznem inearne  napovedovanju - _LPC_, ali na obdelavi signalov, ki je _sinhrono z osnovno periodo_, t.i. postopek _TD-PSOLA_
- Tvorjenje signala z linearnim napovedovanjem izhaja iz osnovnega akusticnega modela govora, ki locuje _vir in filter_
![[zdruzevanje_osnovnih_enot.png]]

## Postopek TD-PSOLA
- Pri tem postopku izvorni govorni signal sumov difonov razdelimo na mnozico prekrivajocih se, kratkocasovnih signalov, ki jih dobimo z oknjenjem izvornega signala (Hammingova okna prek dveh period)
- Oknjene izseke nato po potrebi casovno razmaknemo ali priblizamo, da dosezemo zeleni osnovni ton govora
- Skalirane oknjene izseke nato po potrebi casovno se razmnozujemo ali brisemo, da dosezemo zeleno trajanje posameznih glasov govora
- Koncno tvorimo umetni givirni signal s sestevanjem aporednih oknjenih izsekov

![[postopek_TD.png]]

![[postopek_TD2.png]]

## Tvorjenje prozodijskih parametrov umetnega govora
- _Prozodijo_ (ritem, poudarke, intonacijo) umetnega govora spreminjamo predvsem z nastavljnjem trajanja osnovnega tona posameznih tvorjenih umetnih glasov
- Najzahtevnejsi del izgradnje sintetizatorja umetnega govora je prav samodejno dolocanje prozodijskih parametrov s samodej o racunalnisko analizo poljubnega vhodnega besedila
- Pridobivanje teh parametrov poteka v _vec stopnjah_ od predobdelave besedila, pretvorbe crk v foneme ter nato se dolocanja trajanja intonacije tvorjenih glasov
### Sistem S6TTS za pretvotbo besedil v umetni govor
![[S6TTs.png]]

### Predobdelava besedila
- Iz vhodnega besedila _odstranimo odvecne simbole_, ki ne vplivajo na izgovorjavo besedila
- _Zaporedja stevk_ razvijemo v primeren _grafemski prepis_ (razvoj glavnih in vrstilnih stevnikov)
- Zaporedja _velikih crk_ primerno obdelamo (ugotavljanje, ali gre za naslov ali akronime)
- Za _okrajsave_ dolocimo razsirjen grafemski zapis
- Dolocimo nacin uporabe locil (skladenjska ali neskladenjska raba)
- Pretvorimo _posebne simbole (ideograme)_ v opisni grafemski zapis

Predobdelava Vhodnega besedila podetak v __dveh korakih:__
1.  Iskanje konca povedi - vhodno besedilo preoblikujemo poved za povedjo
2. Predobdelava besed v povedi

![[predobdelava_besedila.png]]
![[grafemski_zapis_vrstilnih_stevnikov.png]]


## Grafemsko foneticni prepis
- Tvorjenje _foneticnega prepisa_ vkljucuje razlicne postopke, kot so:
	- Iskanje foneticnih prepisov danih besed _v slovarju izgovorjav_
	- koartikularni _popravki_ foneticnih prepisov na _besednih mejah_
	- _napovedovanje naglasnega mesta_ v besedah, ki niso vkljucene v dani slovar izgovorjav
	- _samodejna grafemsko fonemska pretvorba_ izvenslovenskih besed
- Najnovejsa metoda pri tvorjenju foneticnega prepisa je navadno uporaba slovarja izgovorjav
- Pridobivanje in priprava dovolj obseznega slovarja izgovorjav zahteva dobto poznavanje govorjenega jezika in njegovega glasoslovja, pri uporabi obstojecih slovarjev pa se pojavlja problem avtorskih pravic

### Dolocanje naglasnega mesta
![[naglasno_mesto.png]]

### Napovedovanje naglasnega mesta
- seznam pripon, ki navadno niso naglasene
- seznam predpon, ki vecinoma niso naglasene
- seznam zacetnic, ki so vecinoma naglasene na prvem zlogu
- seznam zacetnic, ki so vecinoma naglasene na predpredzadnjem zlogu
- seznam zacetnic, ki so vecinoma naglasene na predzadnjem zlogu
- seznam zacetnic, ki so vecinoma naglasene na zadnjem zlogu
- seznam enklitik in proklitik, ki niso naglasene

#### Seznam koncajev in koncnic besed s pogostim naglasom na predzadnjem zlogu
![[seznam_koncajev.png]]

## Produkcijska pravila za grafemsko foneticno pretvorbo
- za pretvarjanje grafemskih nizov v foneticni prepis se uporabljajo _kontekstno neodvisna in kontekstno odvisna_ pravila
- Kontekstno neodvisna pravila _enolicno_ preslikajo grafemski niz v foneticni simbol
- Kontekstno odvisno pravilo sestavljajo niz grafemov, ki ga preslikujemo, njegov _levi in desni_ kontekst ter niz foneticnih simbolov, v katerega se preslika grafemski niz,
- Izerazno moc pravil se povecamo, ce pri vhodnem seznamu grafemskih znakiv uvedemo _dodatne oznake_, s katerimi ponazorimo pravila, ki delujejo nad vecjo skupino glasov
- Vsaka dodatna oznaka opisuje doloceno podmnozico vhodne abecede


## Dolocanje prozodicnih lastnosti umetnega govora
- Pravilna izbira parametrov je zelo pomembna za tvorjenje naravnega in razumljivega govora
- Osnovne tri prozodicne parametre, Frekvenco _F0_, jakost in trajanje je potrebno nastaviti v skladu s segmentno strukturo, slovarjem, skladnjo in semantiko besedila
- Prozodicne lastnosti govora sirse obravnavamo na stirih ravneh uresnicitve, kar ustreza stirim stopnjam v govorni komunikaciji
	- _Jezikovna raven_ poudarjenje dolocenih delov besedila in zaznamovanje meja med deli besedila
	- _Raven izgovorjave_ zaporedje sprememb polozajev in oblik govoril v govornem traktu
	- _Raven akusticne uresnicitve_ osnovna funkcija, jakost in trajanje glasov
	- _Raven zaznavanja_ poslusalec prozodijo zaznava kot premore, dolzino, melodijo, glasnost









# Reference

# Tags
#template 