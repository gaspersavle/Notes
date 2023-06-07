
21.12.2022
11:26
[[# Tags]]
[[# Reference]]

# Teme
- Prileganje dveh nizov vektorjev s casovnim ukrivljanjem
- Prileganje dveh vektorjev znacilk
	- Razpoznavanje loceno govorjenih ukazov
- Preizkusanje razpoznavalnikov vzorcev
	- Preizkusanje z vzorci iz preizkusne mnozice
	- Preizkusaje z vzorci ucne mnozice
	- Druge mere vrednotenja

##  Prileganje dveh nizov vektorjev s casovnim ukrivljanjem
- niza lahko primerjamo tudi neposredno s postopkom _dinamicnega ukrivljanja casa_
- vzorci so vecinoma casovne funkcije
- dva vzorca, numericni funkciji prilegamo tako, da odtipke funkcije f(t) prilegamo z odtipki prototipne funkcije $h(\tau = W(t))$
- razdalja med vzorcema je odvisna tudi od preslikave $\tau = W(t)$, zato jo bomo dolocili tako, da _bo razdalja med nizoma najmanjsa_
-  Operacijo opravljamo  nizoma odtipkov ali znacilk obeh signalov
![[niz_odtipkov.png]]
- preslikavo prve casovne osi na drugo definira niz:
![[preslikava_casovne_osi.png]]
- kjer je vsak w(k) par indeksov, ki ju prilegamo
![[par_indeksov.png]]
- Vsakemu clenu W pripisemo "ceno", ki odraza razdaljo med clenoma para w(k)
- najpogosteje za mero razdalje izberemo kvadrat razlike clenov
- Niz bo najboljsi, ce bo cena preslikave najnizja
![[Pasted image 20221221113857.png]]
![[Pasted image 20221221113905.png]]
![[Pasted image 20221221113914.png]]

- iskanje najboljsega niza W med vsemi oznimi nizi lahko _omejimo z upostevanjem naslednjih pogojev:_
![[pogoji_najboljis_niz.png]]
- __razlika J je lahko 0 le, ce v prejsnjem koraku ni bila 0, torej razlika je lahko 0 le enkrat zapored__

- Najvecje odstopanje W od premice he omejeno, najpogosteje z notranjostjo paralelograma
- zgornjo in spodnjo mejo indeksa J dolocimo, kot funkcijo indeksa i, za vsak i = 1,2,...,P iz obrazcev:
![[obrazci_omejitev_j.png]]
- To omejevanje funkcije W je mozno le, ko velja $P \approx R$
![[Pasted image 20221221114808.png]]
- funkcijo W, ki ji pravimo tudi _funkcija ukrivljanja casa_ dolocimo z iskanjem najcenejse poti med vozliscem (1,1) in vozliscem (P,R)
- To iskanje opravimo _z algoritmom dinamicnega programiranja(nacrtovanja),_ oziroma algoritmom _A*_
![[postopek_ukrivnjanje_casa.png]]
- najmanjsa cena prileganja je $C_{min} (P,R)$
- ker je najmanjsa cena funkcija P in R, vzamemo, da je razdalja med vzorcem in prototipom:
![[najmanjsa_cena.png]]
- funkcijo ukrivljanja casovne osi W lahko obnovimo z vzvratnim obnavljanjem postavljenih kazalcev


## Prileganje dveh nizov vektorjev znacilk
- postopek lahko posplosimo na prileganje 2 nizov vektorjev znacilk
![[poenostavitev_prileganja.png]]
- za mero rzdalje uporabimo kar _evklidovo_
![[evklidovo_primerjanje.png]]

### Zgled poravnave
![[zgled_poravnave_dveh_nizov.png]]
- Bolj kot je svetla barva polja, nizja je cena poravnavem torej nam _modra crta predstavlja pot najmanjsega upora_
- Pri risanju te crte pazimo, da preckamo cim manj rtemnih polj
- sestevki vseh razdalj, torej vseh polj, ki jih precka crta nam poda __Popolno mero podobnosti med dvema nizoma__


### Razpoznavanje loceno izgovorjenih ukazov
- razpoznavamo jih s prileganjem danega govornega vzorca s prototipnim
- vzorec razvrstimo _v razred njemu najbolj podobnega vzorca_, torej _govornega ukaza,ki se danemu najbolj prilega_

## Preizkusanje razpoznavalnikov vzorcev

### Uvod
- razpoznavalnike vrednotimo po hitrosti in zanesljivosti
- v fazi razvoja poizkusimo vec razpoznavalnikov in izberemo najboljsega
- zanesljivost merimo z _oceno verjenosti napacnega razvrscanja_, kar ugotovimo s stevilom napacno razpoznanih vzorcev
![[ocena_zanasljivosti.png]]
- za preizkusanje razpoznavalnika uporabljamo vzorce iz:
	- _preizkusne mnozice vzorcev_ , ce na danem podrocju uporabe razpolagamo z dovolj mocno  testno mnozico $T_M$

	- _ucne mnozice_ vzorcev, ce na danem podrocju ne razpolagamo s testno mnozico
- v prvem primeru moramo poskrbeti za dovolj veliko stevilo testnih vzorcev, ki so po razredih razdeljeni priblizno enako, kot vzorci v vcni mnozici
- v drugem primeru dolocimo _spodnjo in zgornjo_ mejo verjetnosti napacnega razvrscanja, kar dosezemo s precnim preverjanjem in _razmnozevanjem vzorcev_

- ce je v testni mnozici $T_M$ natanko $N_i^*$ statisticno neodvisnih vzorcev iz razreda $C_i$ 
![[testna_mnozica.png]]
- ce je poljuben vzorec $f(x) \in T_i$ napacno razvrstimo z verjetnostjo $P_e^i$ z verjetnostjo $n_i$ , ce velja, da bomo napacno razvrstili toliko vzorcev: $$0 \le n_{i}\le N_i^*$$
![[verjetnost_napacne_razvrst.png]]
kjer je $P(n_i)$ binomska porazdelitev verjetnosti s povprecno vrednostjo in varianco
![[binomska_porazdelitev.png]]
### Preizkusanje z vzorci iz preizkusne mnozice
- najverjetnejsa ocena verjetnosti napacnega razvrscanja preizkusnih vzorcev iz razreda $C_i$ je dolocena kot razmerje med stevilom napacno razvrscenih s stevilom vseh vzorcev iz doticnega razreda
 ![[ocena_pravilnosti.png]]
 - ta ocena je p=nepristranska, kar je njeno matematicno upanje enako $P_e^i$ in trdna, ker je  jena varianca poljubno majhna, ce $N_i^*$ narasca proti neskoncnosti
 ![[varianca_ocene_uspesnosti.png]]
 
- $P_e^i$ ocenimo za vsak razred vzorcev $C_i$, pti i = 1,2,...,M in potem kot oceno verjetnosti napacnega razvrscanja danega razvrscevalnika vzorcev vzamemo kot _utezeno vsoto_
![[utezena_vsota_uspesnosti.png]]
- poskusna mnozica $T_m$ mora biti za zanesljivo dovolj mocna, mejo ko je dovolj mocna dolocimo s spodnjo formulo:
![[ocena_kdaj_je_mnozica_dovolj_mocna.png]]

#### Racunski zgled
![[racunski_zgled_testiranje_razpoznavalnika.png]]

![[racunski_zgled_resitev.png]]


### Preizkusanje z vzorci iz ucne mnozice
- na danem podrocju uporabe ne razpolagamo s testno mnozico
- v takih primerih razpoznavalnik preizkusimo z ucno mnozico $U_m$ tako, da ocenimo spodnjjo in zgornjo mejo verjetnosti napacnega razvrscanja
	- _Spodnjo mejo_ ocenimo tako, da za ucenje razvrscevalnika uporabimovse vzorce ucne mnozice $U_m$, nato pa jih vse uporabimo se enkrat za preizkus razvrscevalnika $T_{m} = U_{m}$ 
	- _Zgornjo mejo_ navadno ocenimo ali s "K- kratnim precnim preverjanjem" ali z razmnozevanjem ucnih vzorcev

- Ugotovljeno je bilo, da za zanesljivo oceno spodnje meje potrebujemo v ucni mnozici vsaj $\frac{3}{5}\cdot n$ vzorcev, kjer je n _stevilo znacilk vzorcev_

#### K- kratno preverjanje
- __Pri k-kratnem precnem preverjanju__ nakljucno razbijemo ucno mnozico vzorcev $U_m$ v K podmnozic
- Po eno podmnozico vzorcev nato uporabimo za preizkus razvrscevalnika, ki smo ga naucili s preostalimi K-1 podmnozicami vzorcev
- Ta postopek ponovinmo k-krat, kri cemer vsako od k podmnozic enkrat uporabljamo na opisan nacin
- Navadno vzamemo K = 10, v primeru da je K = N, kjer je N stevilo vzorcev v $U_m$, pa postopku pravimo _precno preverjanje z izpustitvijo po enega_

#### Razmnozevanje vzorcev
- __Pri nakljucnem razmnozevanju vzorcev__ iz ucne mnozice nakljucno izbiramo in vracamo vzorce, ki se upoprabljajo za ucenje razvrscanja vzorcev
- neizbrane vzorce iz ucne mnozice izberemo kot preizkusne
- Ta postopek ponavadi ponovimo K-krat in pri vsaki ponovitvi _je lahko moc mnozice preizkusnih vzorcev drugacna_
- pri k-tih ponovitvah enega ali drugega opisanega postopka pridobimo ocene $P_e^k$ , pri k = 1,..., K, iz katerih pridobimo skupno oceno verjetnosti napacnega razvrscanja
![[Pasted image 20221221130241.png]]

- pri obeh opisanih postopkih s K-kratnim preverjenjem ocenimo verjetnost napacnega razvrscanja _visje od dejanske vrednosti_
- za oceno dejanske vrednosti napacnega razvrscanja vzamemo _povprecno vrednosti_ med spodnjo in zgornjo mejo
- razilka med zg in sp mejo je odvisna od stevila vzorcev N v ucni mnozici in ta razlika se manjsa, ce stevilo vzorcev v uzni mnozici narasca proti neskoncnosti
![[razlika_med_mejama.png]]

### Druge mere vrednostenja razpoznavalnikov vzorcev
- Pri vrednotenju razvrscevalnika se pogosto podaja tudi razne druge statisticne mere ujemanja med uciteljem in razvrscevalnikom
- Primer taksne mere med nakljucnim in opazenim strinjanjem dveh razvrscevalnikov vzorcev v razrede
- Koeficient k je tako dolocen, kot:
![[dolocitev_k.png]]
- kjer je $P_{a}= 1-P_e$ verjetnost ujemanja med uciteljem in razvrscevalnikom pri razvrscenju vzorcev v razrede in $P_c$ hipoteticna verjetnosti nakljucnega ujemanja med njima
- k ima vrednost 1 pri popolnem strinjanju dveh razvrscevalnikov vzorcev(ucitelja in samodejnega razvrscevalnika) ter vrednost 0, ko je njuno strinajne nakljucno
- Pri isti verjetnosti napacnega razvrsavnja je lahko vrednosti k razlicne, ker je odvisna verjetnosti nakljucnega ujemanja 
- verjetnost nakljucnega strinjanja $P_c$ ocenimo iz verjetnosti, da se oba razvrscevalnika pri danem vzorcu neodvisno nakljucno odlocita za isti razred
- verjetnost $P_c$ tak ocenimo kot vsoto produktov lastnih verjetnosti odlocanja vsakega od razvrscevalnikov za posamezne razrede
![[verjetnst_Pc.png]]
kjer je $P_u(C_i)$ lastna verjetnost, da se za razred $C_i$ doloci ucitelj in $P_r(C_i)$ lastna verjetnost, da se za ta razred doloci razvrscevalnik
#### Racunski zgled
![[racunski_zgled_druge_mere.png]]







- pri dvorazrednem razvrscanju pogosto podajamo tudi druge mere, ki se nanasajo na stiri vrste moznih dogodkov pri ugotavljanju strinjanja _med uciteljem_, ki predpostavljeno podaja resnico in _samodejnim razvrscevalnikom_, ki odlocitve sprejema sam
- pri preizkusu navadno izberemo en razred kot _pozitivni_(napad,okvara,bolezen...), drugega pa kot _negativni_(ni napada, ni okvare, ni bolezni)
- rezultate izvedenih poskusov s stetjem dogodkov zbiramo v t.i. __kontingencno tabelo:__
 ![[kontingencna_tabela.png]]
- iz 4 vrst dogodkov pri izidu poskusa:
	- TP – _pravilno potrjen_  (angl. True Positive, hit),
	-  TN – _pravilno zavrnjen_ (angl. True Negative, correct rejection),
	-  FP – _napačno potrjen_ (angl. False Positive, false alarm, Type I error),
	-  FN – _napačno zavrnjen_ (angl. False Negative, miss, Type II error),

- ... je izpeljano vec razlicnih statisticnih mer, ki se uporabljajo na razlicnih podrocjih, od njih _sta najpomembnejsi:_
	- PPV - _natancnost_ (precision, positive prediction value)
	- TPR - _priklic_ (recall, sensitivity, true positive rate)
![[statisticne_mere.png]]
#### Tolmacenje natancnosti priklica
![[tolmacenje_natancnosti.png]]










- pogosto se uporablja _F-mera_, ki je dolocena kor harmonicno povprecje med natancnostjo in priklicem
![[f_mera.png]]
- mera _Tocnost_ ACC je ekvivalentna oceni verjetnosti pravilnega prepoznavanja $P_a$ 
![[mera_tocnost.png]]
- predlaganih je bilo se vec drugih mer, vendar so izpeljane iz TP, FP, TN in FN, uporabljajo se redkeje na nekaterih podrocjih, kot je medicina

#### Racunski zgled
![[racunski_zgled_mere.png]]
![[racunski_primer_mere_2.png]]
![[racunski_zgle_mere_2.png]]
![[racunski_zgled_mere_3.png]]







 


- Razlicne razpoznavalnike pogosto primerjamo med sabo s primerjavo rezultatov, ki jih pridobimo z njihovim preizkusom z uporabo dane ucne (in preizkusne) mnozice
- pri teh primerjavah, kateri razpoznavalnik je po merah vrednostenja boljsi ali slabsi moramo biti _pozorni na statisticno pomembnost razlik_ med izracunanimi vrednostmi mer
- _Pomembnost teh razlik_ ocenjujemo na enak nacin, kot se to izvaja pri mnogih drugih razlicnih statisticnih analizah podatkov
- navadno pomembnost razlik ocenjujemo iz variance razulatov pri preizkusu prepoznavalnika _z veckratnim precnim preverjanjem_


# Reference
# Tags
#isva #PatternRecogniton #evaluation #learningSet #testSet