# Od robotov do avtonomnih agentov

- _Kako delimo robote glede na uporabo?_
	- industrijski in delovni roboti
	- domaci ali hisni roboti
	- medicinski roboti
	- servisni in strezni roboti
	- vojaski in policijski roboti
	- zabavni roboti
	- raziskovalni roboti

- _Kako delimo robote glede na kinematiko?_
	- stacionarni roboti in robotske roke
	- mobilni roboti s kolesi
	- mobilni roboti z nogami
	- humanoidni roboti
	- leteci roboti
	- plavajoci roboti

- _Kako je definiran avtonomni agent?_
	- Avtonomni agent je sistem, ki je nalozen v neko okolje ali njegov del, to okolje zaznava, v njem deluje in ga skozi cas spreminja v skladu z dolocenimi zastavljenimi cilji

- _Podajte nekaj primerov avtonomnih agentov._
	- Avtonomni roboti
	- programski roboti
	- virtualni asistenti
	- agenti umetnega zivljenja
	- racunalniski virusi in crvi

# Umetna inteligenca

- _Kaj določa inteligenco?_
	- sposobnost _prilagajanja spremenjenim okoliscinam_
	- sposobnost _pomnjenja znanja in njegove uporabe_
	- sposobnost _sklepanja in abstraktnega razmisljanja_
	- sposobnost _ucenja in doumevanja relacij_
	- sposobnost _ovrednotenja in presoje/odlocanja_
	- sposobnost _tvorjenja izvirnih in ustvarjalnih misli_

- _Kako je definirana umetna inteligenca (UI)?_
	- Sposobnost stroja, da opravlja naloge, ki pri cloveskem opravljanju zahtevajo inteligenco

- _Kakšna je razlika med močno in šibko UI_
	- Razlika med mocno in sibko umetno inteligenco je samozavedanje, mocna ga mora vkljucevati, medtem ko se od sibke tega ne pricakuje

- _Katera so podpodročja UI glede na vsebino?_
	-  Umetno zaznavanje
	-  Obdelava naravnih jezikov
	-  Učenje in razvoj
	- Načrtovanje in reševanje problemov
	- Sklepanje in izpeljevanje
	- Robotika
	- Več-agentni sistemi
	- Mehanizmi pomnjenja
	- Predstavitev znanja
	- Razvoj programskih jezikov in orodij

- _Katera so podpodročja UI glede na uporabo?_
	- Medicina
	- Industrijski in proizvodni sistemi
	- Sistemi za pomoč uporabnikom
	- Robotika
	- Izobraževanje
	- Informacijski sistemi
	- Zabavna industrija
	- Preprečevanje kriminala
	- Vojska
	- Vesoljske raziskave
	- Pravni in socialni sistemi
	- Marketing in prodaja
	- Finančni sistemi
- _Katera raziskovalna področja se ubadajo z UI?_
	-  Kombinatorično iskanje
	- Strojni, računalniški vid
	- Ekspertni sistemi
	- Mehko računanje
	- Predstavitev in prikaz znanja
	- Strojno učenje in podatkovno rudarjenje
	- Razpoznavanje vzorcev
	- Obdelava naravnega jezika
	- Umetno življenje
	- Robotika
	- Ambientalna inteligenca in pametni prostori
	- Pametni nadzorni sistemi



# Umetno zaznavanje

- _Kako je definirano področje uporabe?_
	- Podrocje uporabe vsebuje samo tiste objekte iz okolja, ki pripadajo _mnozici objektov razpoznavanja_

- _Kaj so objekti razpoznavanja?_
	- Objekti razpoznavanja so objekti v prostoru in casu, ki jih razpoznavamo, razpoznavamo _zveze in odnose med njimi_.

- _Kaj je razred objektov razpoznavanja?_
	- Razred objektov razpoznavanja je podmnozica tistih objektov z danega podrocja uporabe,  na katere se nanasa nek osnovni stvarni pojem. _NPR:_ _splosni pojem SADJE sestavljajo osnovno stvarni pojmi: JABOLKO, HRUSKA, SLIVA..._

- _Koliko razredov objektov razpoznavanja vsebuje področje uporabe?_
	- Stevilo razredov razpoznavanja na danem podrocju uporabe je doloceno z nalogo razpoznavalnega sistema. _NPR:_ Lahko razpoznavamo sadje samo na  en razred, JABOLKA, vse ostalo sadje pa nas ne zanima in nimamo potrebe po vecih razredih.

- _Kaj je vzorec?_
	- _Vzorec je vsebina cutila oziroma odcitek merilne naprave_, ki daje razpoznavalniku podatke o objektu ali o njegovih medsebojnih zvezah z drugimi objekti.

- _Kaj je razred vzorcev?_
	- Razred vzorcev sestavljajo vzorci, ki so slike objektov iz razreda objektov razpoznavanja. Preslikava objekta iz vzorec mora biti taka, da _tuje razrede objektov preslika v tuje razrede vzorcev_

- _Kako je sestavljena učna množica vzorcev in kdo jo sestavi?_
	- Ucna mnozica vzorcev je koncna mnozica vzorcev z danega podrocja uporabe iz katere se _stroj nauci zvez med oznakami razredov in objekti razpoznavanja_

- _Kako je definirano razvrščanje vzorcev?_
	- Razvrscanje je proces razporejanja vzorcev v razrede, ki so sestavljeni iz ze prej razvrscenih  in medsebojno povezanih vzorcev.

- _Kako je definirano razpoznavanje (preprostih) vzorcev?_
	- Razpoznavanje vzorcev je zadnja faza procesa zaznavanja, v kateri se doloci istovetnost aili velika podobnost nove vsebine cutil, ki je ze bila spoznana in zapomnjena. _Za preproste vzorce je to preslikava, ki vsakemu vzorcu priredi oznako_

- _Kako razpoznavamo vzorce z razvrščanjem?_
	- Pri razpoznavanju z razvrscanjem je vsak razred oznacen z oznako, ki zastopa doloceno podmnozico objektov v okolju. Ce pa za vzorce, ki jih po dolocenem kriteriju ne moremo razvrstiti v nobenega izmed M razredov, uvedemo poseben razred _nerazvrscenih vzorcev_


# Zajem digitalnih slik

- _Kako se zajema slikovne vzorce?_
	- Slikovne vzorce zajemamo s kamero, svetloba ki pade na vsak piksel se pretvori v ustrezen naboj, ki jih zatem vzorci _frame grabber_ in jih zapise kot digitalne podatke

- _Kaj podaja histogram relativnih frekvenc sivih nivojev?_
	- Podaja nam porazdelitev sivih nivojev, oziroma "koliko primerov dolocenega sivega nivoja vsebuje slika"

- _Kakšno obliko ima histogram relativnih frekvenc sivih nivojev slike svetlega izdelka na temni podlagi?_
	- Jistogram pri prakticni uporabi locevanja predmeta od ozadja je histogram sivih nivojev _bi-modalen_, torej ima 2 izrazita vrha, kjer en predstavlja objekt, drug pa ozadje

- _Kako izvajamo razčlenjevanje slik z upragovljanjem?_
	- Iz histograma dolocimo mejo, ki predstavlja prag med sivimi nivoji predmeta in ozadja, s tem lahko  razvrstimo vse piskle v 2 razreda. Ozadje in Predmet

- _Kako se izvaja upragovljanje slik z maksimizacijo informacije?_
	- Ce izvajamo uporagovljanje delimo mnozico zivih nivojev na 2 podmnozici, pri upragovljanju z maksimizacijo informacije postavimo prag tako, da _imamo maksimalno informacijo, ki nam jo predstavljata verjetnostni shemi pojave dolocenega sivega nivoja_
# Dolocanje obrisa podrocja

- _Na katere načine zapišemo področja predmetov na slikah?_
	- Navadno zapisemo, kot seznam naslovov in sivih nivojev vseh tock podrocja predmeta, ki ga zelimo spoznati
	- Lahko ga zapisemo tudi s seznamom tock _obrisov podrocja predmeta_

- _Kako se oblikuje verižna koda obrisa področja na sliki?_
	- Oblikuje se kot seznam smeri, v katerih se moramo premikati, da iz zacetne tocke izsledimo celoten obris objekta in se vrnemo nazaj vanjo.

- _Opišite postopek za določitev obrisov področij._
	- Postopek je sestavljan iz dveh algoritmov, ZT in SO, algoritem ZT doloci koordinate zacetnih tock, algoritem SO pa sledi obrisu, ko je njegova zacetna tocka ze dolocena

- _Kako je določen algoritem SO?_
	- Algoritem SO je dolocen z dvema praviloma, _pravilom leve prioritete_ in _pravilom dolocanja pomoznih oznak_
	- Pravilo leve prioritete opisuje zaporedje preverjanja slikovnih elementov glede na smer vstopa v obris objekta
	- Pravilo dolocanja pomoznih oznak opisuje katero izmed pomoznih oznak priredimo elementu obrisa objekta
![[Pasted image 20230128164840.png]]

- _Kako je določen algoritem ZT?_
	- Algoritem ZT se pomika po elementih slike z leve proti desni, od zgoraj navzdor, za vsak element pa v _seznam preverjenih elementov_ zapisemo primarno oznako na specificno mesto, glede na pomozno oznako tega elementa
		-  Če ima element slike pomožno oznako A, zapišemo njegovo primarno oznako na zadnje prosto mesto na seznamu.
		-  Če ima element slike pomožno oznako D, zbrišemo zadnji vpis v seznamu, vendar le v primeru, ko je primarna oznaka obravnavanega elementa enaka zadnjemu vpisu v seznam, sicer pa ostane seznam nespremenjen.
		-  Če ima element upragovljene slike pomožni oznaki N ali T, ostane seznam nespremenjen.
	- Slikovni element je zacetka tocka obrisa, ce ima pomozno oznako _N_ in primarno oznako, ki ni enaka na zadnje vpisani oznaki v seznamu primarnih elementov


# Opis obrisa s funkcijami Fourierjevih koeficientov

- _Zakaj obrise področij digitalnih slik predstavimo kot diskretno kompleksno periodično funkcijo?_
	- Ker nad njimi sicer ne moremo izvesti Fourierove transformacije, ki nam omogoca odpis obrisa brez popacenja in posledicno slabega razpoznavanja obrisov

- _Kakšen je vpliv premika začetne točke, premika, zasuka in razširitve krivulje obrisa na koeficiente diskretne Fourierjeve transformacije?_
	- 
- _Kako so določene funkcije Fourierjevih koeficientov, ki izničijo
vplivi premika začetne točke, premika, zasuka in razširitve
krivulje obrisa._


# Opis podrocja s parametri sestavne povrsine podrocja

- _S čim opišemo notranjost področij slike?_
	- Zgosceno ga opisemo z znacilkami, ki temeljijo na statistikah prve in druge stopnje

- _Kaj je statistika prvega in kaj statistika drugega reda?_
	- Statistika prve stopnje: Statisticna funkcija posameznih slikovnih elementov
		- povprečna svetilnost (prvi moment)
		- 2., 3. in  4. usredisceni moment
		- entropija (informacija)
	- Statistika druge stopnje: Statisticna funkcija parov slikovnih elementov
		- Značilke, ki temeljijo na porazdelitvi relativnih frekvenc svetilnosti slikovnih elementov, ne vsebujejo informacije o medsebojnem položaju slikovnih elementov področja z enako ali skoraj enako svetilnostjo.

- _Kako so določene matrike frekvenc parov svetilnosti?_
	- Dolocimo jo s pomocjo matrike F frekvenc parov dolocene vrednosti svetilnosti
	- Oznaka #(i,j) nam signalizira verjetnost, da sta elementa s svetilnostima i in j soseda v doloceni smeri na doloceni razdalji

- _Katere značilke opisujejo matrike vezanih verjetnosti svetilnosti?_
	- Energija
	- Kontrast
	- Homogenost
	- Entropija
	- Korelacijski koeficient

# Značilke vzorcev

- _Kaj so značilke vzorcev ?_
	- Znacilke vzorcev so _bistvene lastnosti objektov, ki poudarjajo posebnosti posameznih razredov vzorcev_

- _Zakaj iščemo zgoščen zapis vzorcev?_
	- Zgoscen zapis iscemo, ker je razpoznavanje vzorcev bitka proti racunski kompleksnosti, ki jo pa zmanjsamo s tem da uporabljamo le tiste lastnosti, s katerimi objekte najlazje razlocimo med sabo
	- Z zgoščenim zapisom vzorcev torej _lahko dosežemo njihovo hitrejše razpoznavanje ter učinkovitejše učenje razpoznavalnika_

- _Kako poiščemo najboljšo (pod)množico značilk?_
	-  Najboljsa podmnozica znacilk je tistka, ki v manj razseznostnem prostoru _ne poveca verjetnosti napacnega razvrscanja_ z najboljsim razvrscevalnikom
	- Za kriterijsko funkcijo navadno izberemo eno od mer ločljivosti med razredi vzorcev.
	- Temelji na iskanju vseh tistih hevrističnih značilk, ki ne prispevajo k boljši ločljivosti razredov vzorcev v prostoru značilk.

- _Katere mere razdalje med vzorci poznamo?_
	- Razdalja Minkowskega
	![[Pasted image 20230128172717.png]]
	- City block razdalja
 ![[Pasted image 20230128173932.png]]
	- Cebisevljeva razdalja
	![[Pasted image 20230128174057.png]]
	- Evklidova razdalja
	![[Pasted image 20230128174114.png]]
	- Kosinusna podobnost
	![[Pasted image 20230129205853.png]]


- _Kako merimo ločljivost razredov vzorcev s povprečno razdaljo?_
	- Čim večja bo povprečna razdalja med vzorci različnih razredov, tem večja naj bi bila ločljivost med razredi vzorcev.

- _Opišite postopek izbire značilk "Zaporedno iskanje naprej"?_
	- To je preprost postopek iskanja, kjer na vsakem koraku dodamo trenutni podmnožici značilk tisto meritev, ki najbolj poveča vrednost kriterijske funkcije.

# Razvrščanje vzorcev z umetnimi nevronskimi omrežji

- _Kakšne funkcije uporabljamo pri razpoznavanju vzorcev z odločanjem?_
	- Uporabljamo funkcije, ki delijo n-dimenzionalni prostor v prekrivajoca se podrocja, kjer vsako predstavlja domeno enega razreda vzorcev, te funkcije imenujemo _odlocitvene funkcije_

- _Kako so določene ločilne meje med razredi vzorcev?_
	- Locilne meje, ki locijo podrocja sestavljajo vse tocke, kjer velja pogoj, da sta vrednosti obeh odlocitvenih funkcij enaki pri enakem vzorcu

- _Opišite postopke učenja linearnih ločilnih mej._
	- 
- _Opišite model biološkega nevronskega sistema_
	- Nevronski sistem tvori mnozica podobnih elementov, nevronov ki so vseskozi povezani
	- Nevron sestavljajo:
		- vhodni dendriti,
		- telo nevrona z jedrom
		- izhodni aksoni
	- Drazljaji iz aksona ene celice do dendritov druge celice potujejo preko sinaps

- _Kakšne so lastnosti umetnega modela nevrona?_
	- Sinapse so lahko vzbujalne ali zaviralne
	- Nevron sprejema signale iz drugih nevronov, le-te nato integrira in lahko rodi lasten signal, ki potuje po aksonu iz celicnega telesa
	- Rojevanju signala v celicnem telesu pravimo vzig nevrona
	- Kdaj se bo po vzigu nevron ponovno vzgal je odvisno od stevila vzbujalnih in zaviralnih vhodov v nevron in od praga nevrona
	- Visji bo prag nevrona, vec vzbujevalnih impulzov je potrebnih, da nevron vzge

- _Kako razpoznavamo vzorce s triplastnim perceptronom?_
	- 



- _Kako učimo triplastni perceptron?_
	1. Vsem utezem povezav priredimo enakomerno porazdeljeno nakljucno vrednost, navadno iz razmaka {-0.5, 0.5}, vendar nobena od teh utezi ne sme biti na zacetku enaka nic, ker bo tako ostala nic tekom celotnega postopka ucenja. Postavimo k = 1.
	2. V k-ti ponovitvi postopka ucimo omrezje s k-tim vzorcem iz ucne mnozice. Za vzorec x(k) dolocimo zelene izhode vrednosti nevronskega omrezja. Navadno postavimo ti(k) = 1, ce je dan vzorec iz razreda Ui. Vse ostale t(k) pa postavimo na vrednosti nic. Ucenje z vzorci iz ucne mnozice ponavljamo toliko casa, dokler se utezi nevronov ne umirijo
	3. Izracunamo izhode nevronov prve, druge in tretje plasti
	4. Izracunamo popravke utezi nevronov tretje plasti in jih popravimo
	5. Izracunamo se popravke nevronov druge in prve plasti in popravimo tudi te utezi
	6. postavimo k = k + 1 in se vrnemo na korak 2

- _Kaj je na vhodu in kaj na izhodu triplastnega perceptrona?_
	- Na vhodu perceptrona je vzorec, razdeljen na znacilke, na izhodu pa razred v katerega sodi.

# Sistem "kamera - robotska roka“

- _Zakaj je pomembna koordinacija oči in rok?_
	- Ce okolje zaznavamo z vidom je koordinacija pomembna, ker sicer aktuator ne bo vplival na iste tocke, kot jih zaznava kamera

- _Kateri dve preslikavi določata geometrični model kamere?_
	- Perspektivna projekcija tocke _iz trirazseznega prostora na dvorazsezen senzor_
	- Preslikava tocke _iz metricne slikovne ravnine na nemetricno digitalno slikovno ravnino_
	

- _Najmanj koliko koordinat točk moramo poznati v prostoru robota za umerjanje sistema „kamera – robotska roka“?_
	- 6

- _Kako določimo lego predmeta v prostoru robota?_
	- Ce poznamo elemente matrike M in koordinati (u,v) na senzorju, lahko dolocimo lego predmeta v prostoru robota s tem da _iz formul za izracun koordinat u in v izpostavimo m34 = 1 in zr = 0, tako dobimo preprost sistem 2 enacb in ju resimo za neznanki xr in yr._
	![[Pasted image 20230129212551.png]]

- _Kako določimo notranje in zunanje parametre kamere?_
	- Iz elementov matrike M lahko izracunamo notranje in zunanje parametre kamere, to so elementi matrik KP in A
	![[Pasted image 20230128190848.png]]
	![[Pasted image 20230128190907.png]]
	
- _Katere druge probleme umerjanja kamer rešujemo na področju strojnega vida._
	-  Nelinearnosti opticnega sistema kamer

# Zajemanje, razčlenjevanje in parametrično opisovanje vzorcev govornega signala

- _Kako se razčleni govorni signal?_
	- Navadno ga razclenimo na osnovi merjenja kratko-casovne glasnosti govora in stevila prehodov skozi niclo. Tako lahko govorni signal razclenimo na povedi, med katerimi so kratki premori zaradi dihanja.

- _Katere enote razpoznavanja govora se uporablja?_
	- Uporabljamo odseke, ki so zaporedno prekrivajoce-se kratki odseki z enakim trajanjem. So krajsi od najkrajsega glasu a dovolj dolgi, da odrazajo kratkocasovne spektralne znacilnosti izsekov

- _Katere značilke najbolj pogosto uporabimo za opis enot razpoznavanja govora?_ 
	- Moc ali glasnost
	- Frekvenca osnovnega tona
	- Resonancne frekvence

- _Kaj je to homomorfna analiza izseka govornega signala?_
	- S homomorfno analizo poskusamo iz govornega signala pridobiti locena signala vzbujanja govornega sistema u(n) in njegovega odziva na enotin impulz h(n)

- _Kako se izračuna koeficiente melodičnega kepstra?_
	- Koeficiente izracunamo _z logaritmom povprecnih moci frekvencnih obmocij_, razdeljenih po melodicni delitvi. Namesto logaritma mocnostnega spektra

- _Kako opišemo dinamične značilnosti govora?_
	- Dinamicne znacilnosti prvega reda so definirane kot razlike med znacilkama istega signala, vendar na izsekih, ki sta med sabo oddaljena med 2 in 6 odsekov
	- Dinamicne znacilnosti drugega reda so definirane kot razlike med znacilkami prvega reda, ki so prav tako med sabo oddaljene med 2 in 6 segmentov

- _S kakšnimi modeli navadno modeliramo govor?_
	- Govor navadno modeliramo s kaskado deterministicnih, nedeterministicnih in verjetnostnih koncnih avtomatov stanj.

- _Kakšne so posebnosti modeliranja slovenskega govora?_
	- Posebnost modeliranja slovenskega govora je sirina izgovorjave samoglasnika, primer: nAto, natO, ki lahko popolnoma spremeni pomen besede

# Razvrščanje vzorcev s prileganjem

- _Na kakšen način izvajamo razvrščanje vzorcev s prileganjem?_
	- Nacin razvrscanja s prileganjem temelji na merjenju podobnosti med vzorcem, ki ga razpoznavamo in znacilnimi predstavniki (prototipi) razredov vzorcev iz ucne mnozice
	- Vzorec razvrstimo v razred, katerega znacilni predstavnik mu je najbolj podoben

- _Kako razvrščamo s prileganjem vzorce - množice vrednosti značilk?_
	- Postopke razvrscanja vzorcev s prileganjem delimo:
		- Glede na zapis ucne mnozice vzorcev v pomnilniku, razlocimo postopke, ki _hranijo celotno ucno mnozico_ in postopke, ki _hranijo le znacilne predstavnike razredov vzorcev_
		- Glede na stevilo najbolj podobnih vzorcev v pomnilniku, ki jih upostevamo pri razvrscanju. Locimo primera, ko _upostevamo samo najbolj podoben vzorec_ in primer, ko upostevamo _k > 1 najbolj podobnih vzorcev_

- _Kaj določa pravilo razvrščanja "najbližji sosed" (1-NN)?_
	- Pravilo doloca, da vzorec razvrstimo v razred, ce mu je med vsemi vzorci iz ucne mnozice najbolj podoben vzorec iz tega razreda

- _Zakaj je pravilo razvrščanja 1-NN posplošeno na pravilo razvrščanja "k-najbližjih sosedov“?_
	- Ker pravilo, ki uposteva samo najbolj podoben vzorec ne izkorisca dovolj informacije, ki jo vsebuje ucna mnozica

# Razvrščanje nizov vektorjev značilk s prileganjem

- _Kako preslikamo niz vektorjev značilk v niz simbolov?_
	- Niz vektorjev  preslikamo v niz simbolov s postopkom _vektorske kvantizacije_

- _Opišite osnovno zamisel postopka vektorske kvantizacije._
	- Kvantizacijo odtipkov lahko posplosimo na bloke odtipkov
	- Vektorsko kvantizacijo opravimo tako, da zapisemo blok sosednjih odtipkov kot vektor x, ta predstavlja tocko v n-razseznem prostoru, ki ga delimo na _PARCELE_, meje parcel so daljice, ki _so enako oddaljene od sredisc sosednjih parcel_. 
	- Ce je dana tocka najblizje srediscu neke parcele, jo zapisemo s kodo/_znakom_ te parcele

- _Kako razvrščamo nize znakov s prileganjem?_
	- Vzorce, ki smo jih zapisali z nizi znakov, razvrscamo s prileganjem tako, da merimo podobnost med njimi in med vzorci iz ucne mnozice, ki so prav tako zapisani z nizi znakov iz abecede

- _Kako merimo podobnost dveh nizov znakov?_
	- Podobnost dveh nizov znakov najbolje merimo z Levenshteinovo razdaljo
	- Levenshteinova razdalja je dolocena kot najmanjse stevilo transformacij, potrebnih za preslikavo enega niza znakov v drugega

- _Kako je določena utežena Levenshteinova razdalja med dvema nizoma znakov?_
	- Utezena Levenshteinova razdalja je dolocena na podlagi razlicne "cene" preslikav znakov v danem nizu. Torej je utezena levenshteinova razdalja _vsota cen preslikave enega niza v drugega_

- _Kako merimo podobnost dveh nizov vektorjev značilk s časovnim ukrivljanjem._
	- 

# Preizkušanje razpoznavalnikov vzorcev

- _Katere vzorce lahko uporabimo za preizkušanje razpoznavalnika vzorcev?_
	-  Za preizkusanje razpoznavalnika lahko uporabimo vzorce iz preizkusne mnozice $T_{M}$ ali iz ucne mnozice $U_{M}$, ce na danem podrocju uporabe ne razpolagamo s preizkusno mnozico.
	
- _Kako je določena najbolj verjetna ocena verjetnosti napačnega razvrščanja preizkusnih vzorcev iz nekega razreda?_
	- Najbolj verjetna ocena verjenosti napacnega razvrscanja je dolocena kot razmerje med stevilom napacno razvrscenih vzorcev in stevilom vseh preizkusnih vzorcev iz razreda

- _Koliko najmanj neodvisnih vzorcev moramo imeti na razpolago, da lahko trdimo z verjetnostjo 0,95, da je trditev, da dejanska verjetnost napačnega razvrščanja 𝑃𝑒 ne presega ocenjene verjetnosti za več kot 0,2 ⋅ 𝑃𝑒 , pravilna?_
	- $$N^{*} = \frac{100}{P_{e}}$$

- _Kako ocenimo spodnjo in zgornjo mejo verjetnosti napačnega razvrščanja, pri preizkusu razpoznavalnika z učno množico vzorcev?_
	- Zgornjo mejo navadno ocenimo ali s _K-kratnim navzkriznim preverjanjem_ ali z razmnozevanjem ucnih vzorcev (bootstraping)
	- Spodnjo mejo dolocimo tako, da za ucenje razvrscevalnika uporabimo vse vzorce iz ucne mnozice, nato pa jih vse uporabimo se enkrat za preizkus razvrscevalnika $T_{M}= U_{M}$

- _Katere druge mere vrednotenja razpoznavalnikov vzorcev še poznamo?_
	- Cohenov koeficient kapa
	- F- mera
	- Mera tocnosti ACC
	- PPV - natancnost (precision, positive predictive value)
	- TPR - priklic (recall, sensitivity, true positive rate)

- _Kakšno mero podaja Cohenov koeficient kapa (𝜅)?_
	- Koeficient kapa, na splosno podaja razmerje med nakljucnim in opazenim strinjanjem dveh razvrscevalnikov vzorcev

# Tvorjenje umetnega govora

- _Razložite, zakaj je tvorjenje umetnega govora pomembna sestavina umetnih inteligentnih sistemov._
	- Ker bi morali inteligentni sistemi komunicirati z ljudmi na njim naraven nacin, govor pa je nam najnaravnejsi nacin komunikacije

- _Podajte primere takšnih sistemov in razložiti vlogo umetnega govora v teh sistemih._
	- Virtualni asistenti
	- Tik tak blagajna
	- Telefonski odzivniki

- _Opišite osnovne značilnosti tvorjenja govora._
	- Govor _lahko smatramo kot nekaksno glasbilo_ iz druzine pihal in trobil
	- Za tvorjenje govora ponavadi _uporabljamo izdisni zrak_, ki se mimo glasilk pretaka v ustno ali nosno votlino
	- _Z napetostjo misic ki obkrozajo glasilke dosezemo nihanje z doloceno frekvenco_, ko se skoznje pretaka zrak
	- Zvok _dobi poseben zven, odvisen od odprtine skozi katero potuje_ (zrelo, ustna votlina, nosna votlina)
	- Glasovi ki jih ustvarimo z nihanjem glasilk so _zveneci glasovi_
	- Glasovi, ki jih tvorimo s turbulenco, pri ozanju dolocenih poti, skozi katere potuje izdisni zrak pravimo _sumenje_, ti glasovi so _nezveneci_

- _Kateri je najbolj enostaven način tvorjenja umetnega govora in katere so njegove slabosti?_
	- Najenostavnejsi proces tvorbe govora je _sintetizator z zdruzevanjem osnovnih enot_, navadno deluje tako, da lepi skupaj _difone_, ki predstavljajo prehode med zaporednimi glasovi, njegova slabost so spektralne nezveznosti, ki se pojavijo na zlepkih

- _Opišite zasnovo sistema za tvorjenja umetnega govora v slovenščini?_
	- ![[Pasted image 20230129172629.png]]
	- ![[Pasted image 20230129172646.png]]

- _Katere komponente takšnega sistema je najtežje razviti in imajo velik vpliv na naravnost umetnega govora?_
	- Najtezje je razviti samodejno dolocanje prozodijskih parametrov (ritem, poudarki, intonacije)

# Govorna komunikacija "človek - stroj“

- _Kaj vse se uporablja za vhod in kaj za izhod v sistemih za komunikacijo „človek-stroj“?_
	- Za vhod se uporablja: dotikanje, tipkanje, pisanje, geste, menijske izbire...
	- Za izhod se uporablja: zvozne signale, graficne prikazovalnike, animirane graficne in mehanske like, svetila...

- _V katerih primerih in zakaj je govor človeku najbolj prikladen način komunikacije s stroji?_
	-  Primeren je, ko mora clovek med interakcijo s strojem zraven se nekaj delati, tikati ali opazovati.

- _Kateri so osnovni gradniki sistema za govorno komunikacijo „človek-stroj“?_
	- Razpoznavalnik govora
	- Sistem za dialog
		- Pomenski analizator
		- Upravljalec dialoga
		- Generator sporocil
	- Sintetizator govora

- _Katere vrste dejanj v dialogu navadno obravnavamo?_
	- Informacija o stanju
	- Ukazi
	- Obveze uporabnika
	- Izrazi dusevnega stanja uporabnika
	- Deklaracije novega stanja okolja s strani uporabnika
	![[Pasted image 20230129173506.png]]


- _Kako navadno modeliramo upravljavca dialoga?_
	- Modeliramo ga s 3 komponentami:
		- Enota za pomensko analizo sporocil, ki isce besede ali fraze v vhodnem besedilu, ki predstavljajo eno izmed podprtih pomenskih kategorij
		- Enota za generiranje sporocil, ki preslika sistemska dejanja v dialogu v besedna sporocila v naravnem jeziku

- _Opišite glavne faze načrtovanja sistema za dialog._
	- Zbiranje in dokumentiranje primerov dialogov izbranega podrocja ter groba zasnova sistema
	- Simulacija delovanja sistema za dialog, kjer delovanje sistema delno ali b celoti nadomesti cloveski operater
	- Analiza zbranega gradiva
	- Podrobna zasnova in popravki strukture postopka za upravljanje dialoga
	- Preizkusanje sistema

- _Katera programska orodja obstajajo za razvoj sistemov za govorno komunikacijo „človek-stroj“?_
	- XML
	- VoiceXML

#isva #izpitno2023 #ustno