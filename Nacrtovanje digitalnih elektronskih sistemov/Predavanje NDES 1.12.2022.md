01.12.2022
22:33
[[# Tags]]
[[# Reference]]

# Teme
- staticna __CMOS__ logika
- Staticen komplementarni CMOS
- vzporedna in zaporedna vezava
	- NMOS: logicen pogled (boolova algebra)
	- PMOS: logicen pogled (boolova algebra)
- padci preklopnih napetosti
- kompleksna CMOS vrata
	- lastnosti CMOS tehnologije [[#Lastnosti CMOS]]
- model preklopnih zakasnitev
- dimenzioniranje tranzistorjev glede na zakasnitve
- vpliv razvejanosti na zakasnitve
	- vpliv __FAN-IN__
	- vpliv __FAN-OUT__
- tehnike pospesevanja integriranih vezij 
	1. velikost tranzistorjev ^3abab5
	2. vrstni red tranzistorjev ^aa2b7e
	3. alternativna struktura logike ^2afde3
	4. izolacija FAN-IN in FAN-OUT vpliva ^67d2df
- __psevdo logika__ oziroma __Ratioed Logic__
	- psevdo NMOS
	- adaptivno breme
	- diferencialna, kaskadno-napetostna logika __(DCVSL)__


## Staticna komplementarna CMOS logika
- dualnost __PULL-UP__ in __PULL-DOWN__ dela vezja
- CMOS je po naravi dualen, to je zapisano ze v imenu
![[CMOS_model.png]]

## Vzporedna in zaporedna vezava CMOS logike
### NMOS
- NMOS tranzistorji nosijo __mocno niclo "0"__ in __sibko enico "1"__
- NMOS tranzistor se odpre, ko dobi na vhodu visoko stanje, takrat se "stikalo sklene"
![[boolova_NMOS.png]]

### PMOS
- PMOS tranzistorji nosijo __mocno enico "1"__ in __sibko niclo "0"__
- PMOS tranzistor se odpre, ko dobi na vhodu nizko stanje, takrat se "stikalo sklene"
![[boolova_PMOS.png]]

## Padci preklopnih napetosti
### Pull-up network PUN
- zato, da je N-kanalni tranzistor odprt, mora biti napetost $U_{gs}$ vecja od preklopne napetosti tranzistorja $U_t$. PUN vezje polni izhodno kapacitivnost $C_l$  proti vrednosti $U_{dd}$ , vendar je ne more doseci. Na primer, ce je napajalna napetost $U_{dd}=2,5V$ in preklopna napetost $U_t=0,5V$, tranzistor bo lahko $C_l$ napolnil le na 2V, saj bo pri tej vrednosti $U_{gs} =0V$ , torej manjsa od preklopne napetosti, kar pomeni, da se bo tranzistor zaprl in kondenzator prenehal polniti, s tem se je efektivno povisala preklopna napetost tranzistorja kot posledica kapacitivnosti bremena $C_l$
![[premik_preklopne_nap_PUN.png]]
### Pull-down network PDN
- zato, da je P-kanalni tranzistor odprt, mora biti absolutna vrednost napetosti $U_{gs}$ vecja od preklopne napetosti tranzistorja $U_t$. PDN vezje prazni izhodno kapacitivnost $C_l$  proti vrednosti 0V, vendar je ne more doseci. Na primer, ce je napetost na izhodni kapacitivnosti$C_l$ , $U_{CL}=2,5V$ in preklopna napetost $U_t=-0,5V$, tranzistor bo lahko $C_l$ spraznil le na 0,5V, saj bo pri tej vrednosti $U_{gs} =0V$ , torej absolutno manjsa od preklopne napetosti, kar pomeni, da se bo tranzistor zaprl in kondenzator prenehal prazniti, s tem se je efektivno znizala preklopna napetost tranzistorja kot posledica kapacitivnosti bremena $C_l$
![[premik_preklopne_nap_PDN.png]]
#### Zgledi
##### Zgled NAND
![[izvedba_CMOS_NAND.png]]
###### Zgled NOR
![[izvedba_CMOS_NOR.png]]
## Kompleksna CMOS vrata
![[kompleksna_CMOS_vrata.png]]
### Konstrukcija kompleksnih CMOS vezij
![[konstrukcija_kompleksnih_CMOS.png]]
### Diagram poteka signala prek tranzistorjev
![[diagra_poteka_kompl_CMOS.png]]
## Lastnosti CMOS
- visoke sumne meje _Full rail-to-rail swing_
- logicni nivoji so neodvisni od velikosti komponent _Ratioless_
- v stabilnem stanju (ko ne poteka preklop) ima vedno povezavo na napajanje ali maso, ima  _Nizko izhodno impedanco_
- _Izjemno visoka vhodna impedanca_, vhodni tok v staticnem stanju je skoraj nic
- Nima _Staticne porabe moci_
- Propagacijska zakasnitev je funkcija izhone kapacitivnosti in upornosti tranzistorjev
## Model preklopnih zakasnitev
### Vhodno zaporedje
- tranzistorje zacnemo predstavljati s stikalom in njegovo interno upornostjo
![[pretvorba_tranzistor_stikalo.png]]
- zakasnitev je odvisna od vhodnih vzorcev, torej zaporedja v katerem vzbujamo tranzistorje v CMOS vratih
	- __Ob prehodu z " 0 " na " 1 ":
		- _Oba vhoda nastavimo na " 0 " istocasno_:
				$$t_{PHL}=0,69\cdot\frac{R_p}{2}\cdot C_l$$
		-  _Samo en vhod nastavimo na "0"_:
				$$t_{PHL}=0,69\cdot R_p\cdot C_l$$
	- __Ob prehodu z " 1 " na " 0 ":
		-  _Oba vhoda postavimo na " 1 " istocasno_:
			- zaradi narave NAND vezave moramo nastaviti oba tranzistorja na "1 "
				$$t_{PHL}=0,69\cdot2R_p\cdot C_l$$
![[zakasnitveni_model_NAND.png]]
- zakasnitve glede na vhodno kombinacijo
![[zakasnitve_CMOS_NAND_kot_funkcija_vhodne_kombinacije.png]]

## Velikost tranzistorjev
- Pri zaporedni vezavi 2 tranzistorjev se njuni interni upornosti zaporedno vezeta, zaradi dualnosti CMOS logike, sta ta 2 tranzistorja v nasptotni polovici logicnih vrat vezana vzporedno, torej se tudi njuni interni upornosti vezeta vzporedno. Zaporedna vezava rezultira v dvakratni upornosti, medtem ko vzporedna v polovicni, zaradi tega bo imel zaporedno vezani del vezja 4x vecjo zakasnitev kot vzporedno vezan del, na to se pomnozijo se razlike med zakasnitvijo PMOS in NMOS, zato moramo dolocene tranzistorje povecati, da uskladimo zakasnitev med preklopom z 0 na 1 ter priklopom med 1 in 0
![[velikost_CMOS_tranzistorjev.png]]
![[velikost_CMOS_tranzistorjev_2.png]]

## Fan-in vpliv
- propagacijska zakasnitev se hitro poslabsa s spremembo fan-ina, v najslabsem primeru __s kvadratom stevila vhodnih llinij oziroma fan-ina__ 
- vzrok sta povecana upornost zaradi zaporedne vezave tranzistorjev v PDN delu vezja, z njimi seveda pridejo tudi interne upornosti, ki prav tako skodijo zakasnitvi
$$t_{pHL}=0.69 \cdot R_{eqn}(C_1+2C_{2}+ 3C_{3}+ 4C_L)$$
![[fan_in_vpliv_zakasnitve_CMOS.png]]
## Fan-out vpliv
- propagacijska zakasnitev se poslabsa zaradi vhodnih kapacitivnosri dodatnih gradnikov, ki jih cutimo na izhodu trenutnega gradnika. Te vhodne kapacitivnosti se pristejejo k bremenski kapacitivnosti $C_L$
$$t_{P} = a_{1}\cdot FI + a_{2\cdot}FI^{2}+ a_{3}\cdot FO$$
$$FI = Fan \space In \quad FO = Fan \space Out$$
- kjer __FI pomeni fan in__, __FO pa pomeni fan out__
## Tehnike pospesevanja CMOS integriranih vezij
1.  [[#Velikost tranzistorjev]]
	-  progresivne velikosti (sirine vrat) zaporedno vezanih tranzistorjev lahko zmanjsajo zakasnitev za vec, kot 20%, vendar vpliv te metode upade z uporabo manjse tehnologije vezja
	- tranzistor najblizje izhodu ima lahko najozji kanal, saj se bo skozenj praznil le $C_L$, torej bo skozenj tekel najmanjsi tok, najsirsa vrata mora imeti tranzistor najblizje ozemljitvi, saj se bodo skozenj praznile vse interne kapacitivnosti poleg izhodne kapacitivnosyi $C_L$
	![[progresivne_velikosti_tranzistorjev.png]]
2. __Vhodno zaporedje__
	- Zakasnitev je odvisna od vhodnega vzorca
	- Ce hkrati sklenemo obe stikali se $C_{L}$ sprazni prek internih upornosti obeh stikal
	- Ce hkrati sklenemo obe stikali _pull up dela vezja_, se $C_{L}$ napolni prek obeh internih upornosti, torej efektivno "cuti" polovicno upornost. Izhodna kapacitivnost se _napolni hitreje_
	- Ce sklenemo le enega izmed stikal v pull up delu, se $C_{L}$ napolni le prek ene interne upornosti, torej je polnilni tok nizji in _se kapacitivnost napolni kasneje_.
![[Pasted image 20230125223244.png]] ^765712
3. __Alternativna struktura logike__ ^e1c9bd
	- namesto ene 8 vhodne NAND funkcije, lahko naredimo trinivojsko strukturo sestavljeno iz 2-vhodnih gradnikov in s tem prihranimo nekaj zaporedno vezanih tranzistorjev, s cimer pospesimo vezje
	![[alternativna_logika.png]]
4. __Izolacija fan-in in fan-out__
	- z uporabo t.i. bufferjev lahko izoliramo vpliv fan outa. Ce npr za svoj gradnik povezemo 2 inverterja lahko zaradi bremenske kapacitivnosti $C_L$ prilagodimo velikost le enega tranzistorja, ki je del inverterja, namesto prilagoditve 4 tranzistorjev v NAND vezju
![[izolacija_razvejanosti_CMOS.png]] ^badc8a
## Psevdo logika (ratioed logic)

^bbda7f

- zgrajena iz N-kanalnih tranzistorjev in upornega bremena s ciljem, da zmanjsa stevilo komponent (tranzistorjev) v primerjavi s komplementarnim CMOS
- izhodna napetost visokega stanja je enaka napajalni napetosti integriranega vezja $$U_{OH} = U_{DD}$$ $$U_{OL} =U_{DD} \frac{R_{PDN}}{R_{PDN}+ R_L}$$
	- __KJER VELJA__
		- $R_{PN}$ je upornost PDN med delovanjem
		- $R_L$ je upornost uporovnega bremena
-  ta nacin izvedbe integriranih vezij ima asimetricen odziv, kar pomeni, da se prehod $1 \Rightarrow 0$ zgodi hitreje, kot pa $0 \Rightarrow 1$
- vezje ima zaradi upora, vezanega na $U_{DD}$ staticno porabo moci
- $t_{PL} = 0,69 \cdot R_{L} \cdot R_C$ 
### Psevdo NMOS
![[psevdo_NMOS.png]]
- manjsa povrsina in manjse breme, kot pri "ratioed" logiki, vendar vseeno obcutimo staticno porabo moci
- __VELJA:__
	- $U_{OH} = U_{DD}$
	- $k_{n}\cdot[(U_{DD}-U_{TN})\cdot U_{OL}-\frac{U_{OL}^{2}{2}]}= \frac{k_{P}}{2} \cdot (U_{DD}-|U_{TP}|)^2$
	- $U_{OL} = (U_{DD}-U_{TN}) \cdot \left[1- \sqrt{1-\frac{k_P}{k_{N}}}\right]; U_{T}= U_{TN}= |U_{TP}|$
- psevdo NMOS __PRENOSNA FUNKCIJA__
![[psevdo_NMOS_pren_f.png]]
### Adaptivno breme
![[adaptivno_breme.png]]
- M1 je veliko vecji od M2, z izbiro kombinacije vhodov lahko prilagodimo hitrost vezja za razlicne kombinacije vhodov, _na primer:_
	- ce odpremo le ena izmed vrat A, B, C in D bo upornost celotne poti do napajanja najvecja mozna, ce odpremo vsa 4 pa kar 4x manjsa, kar pomeni hitrejse praznjenje bremenske kapacitivnosti.
	- zato imamo na izbiro oba tranzistorja, saj lahko pri kombinaciji, ki ima nizjo upornost z uporabo manjsega tranzistorja M2 upocasnimo vezje, da dosezemo zakasnitve, ki so konsistentne z ostalimi gradniki
### DSVL: diferencialna, kaskadno-napetostna logika
- ta tip logike je konstruiran iz dualnih parov tranzistorjev in ima 2 izhoda, en je negiran, en pa ne-negiran
- prednost take tehnike izdelave vezja je, da v nasprotju s CMOS __eliminiramo velike PMOS tranzistorje__ in imamo tako vecjo logicno gostoto, prav tako pa __nimamo staticne porabe moci__
![[DCVSL_XNOR.png]]
![[pravilnostna_tabela_xnor_DCVSL.jpg]]
![[odzivi_DCVSL.png]]

# Reference
https://journals.indexcopernicus.com/api/file/viewByFileId/363544.pdf

# Tags
#ndes #chip #cmos #kombinacijskaVezja