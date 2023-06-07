
07.12.2022
19:20
[[# Tags]]
[[# Reference]]

# Teme
- Regulacijski bloki
- Izvedba PID regulatorja
- Vezave clenov PID
- Racunalniska izvedba PID
- Stopenjske izvedbe PID regulatorja

## Regulacijski bloki
- Locimo vec vrst regulacijskih blokov
### Stopenjski regulacijski bloki
- Dvo ali tro-polozajna regulacija, uporablja se pri vodenju pocasnih procesov, npr. :
	- regulacija temperature
	- nivo tekocine
![[stopenjski_regulacijski_bloki.png]]
### Zvezni regulacijski bloki
- regulacijski algoritem PID
	- deluje proporcionalno, integrirno in deferencirno
	- clene P, I in D lahko vezemo na razlicne nacine
	- poznamo vec razlicnih tipov vhodnih signalov
		- regulirna velicina/reference
		- pogresek
		- loceni vhodi v P, I in D clene
	- vec tipov izhodnih signalov
		- __Zvezni:__ 4-20 mA, 10V
		- __Pulzin:__ dvostanjski, trostanjski
	- Pri razlicnih proizvajalcih obstajajo razlicne izvedbe PID algoritma
## Izvedba PID regulatorja
- izhod PID je setavljen __iz utezenih prispevkov posameznega clena__
![[formula_PID.png]]
## Vezave clenov PID
- modifikacije standardne PID vezave
![[standard_PID.png]]
-_PI-D:_
![[mod_PI_D.png]]
- _I-PD_
![[mod_I_PD.png]]
- modifikaciji se enako vedeta pri motnji v procesu, vendar imata drugacne lastnosti pri odzivu na spremembo referencne vrednosti
## Racunalniska izvedba PID algoritma
![[pid_algoritem_shema.png]]
### Zvezni in vzorceni signali
- V praksi veliko delamo z vzorcenimi signali zaradi digitalne narave delovanja racunalnikov ter njihove obstojnosti v industrijskem okolju z motnjami in potencialno dolgimi vodili do PLC
![[zvezni_in_vzorceni_signali.png]]
- pri diskretizaciji se operacija __integral pretvori v vsoto__
	- $\int_{0}^{t} e(\tau)d\tau \doteq T_0\sum_{i=1}^{k}e(i-1)$
	- kjer je e __pogresek regulatorja__ (razlika med referenco in izhodno vrednostjo), $T_0$ pa perioda vzorcenja, oziroma cas , ki potece od enega do drugega vzorca
### Rekurzivna oblika PID algoritma
- Da dobimo rekurzivno obliko odstejemo $u(k)-u(k-1)$ 
![[rekurzivna_oblika_pid.png]]
![[diskretni_pid_algoritem.png]]

![[alt_diskretni_pid_algoritem.png]]
![[alt_rekurzivna_oblika_pid.png]]
### Odziv na stopnicasto spremembo pogreska
![[odziv_na_step_spremembo_vh.png]]
$$q_{0}+q_{1}+ q_{2} = K_{p}*\frac{T_0}{T_i}$$
### Relacije med parametri
- Pozitivna diferencialna konstanta 
	- $q_{0}+ q_{1}< 0$ oz $q_{1}< -q_0$
- Pozitivna integrirna konstanta
	- $q_{0}+ q_{1}+q_{2}>0$ oz $q_{2}> -(q_{0}+q_{1})$
	- $q_{0}> 0$
- ojacanje P, I in D clena
	- $K_{p}+ q_{0}= q_{2}$           $C_{I}=\frac{T_0}{T_{i}}= \frac{q_{0}+ q_{1}+ q_2}{K_p}$             $C_{D}= \frac{T_D}{T_0} = \frac{q_2}{K_p}$
	- oz. $K_{p} = (q_0-q_2)/(1+\frac{T_0}{T_I})$  ce uporabljamo alternativno obliko
### Izvedba diskretnega PID algoritma
- algoritem se izvaja v zanki, katere izvajanje je usklajeno s taktom vzorcenja $T_0$
- __osnovni koraki:__
	1. vzorcenje procesa, primerjava z zeleno vrednostho in izracun pogreska
	2. izracun regulirnega signala
		![[izracun_reg_signala.png]]
	3. prenos regulirnega signala na izhod regulatorja
	4. cakanje na nov trenutek vzorcenja in zatem vrnitev na 1. korak
- __Primer z daljsim casom vzorcenja:__
	- vidimo, da obstajajo velika odstopan ja med odzivi  in regulirnimi signali
![[primer_daljse_vzorcenje.png]]
- __Primer s krajsim casom vzorcenja:__
	- vidimo zelo majhna odstopanja med razlicnimi diskretnimi regulirnimi in izhodnimi signali
![[primer_krajsi_vzorcni_cas.png]]
### Izbira casa vzorcenja
- cas vzorcenja izbiramo primerno na podlagi __zaprtozancnega odziva__
- _Osnovna zveza:_
	- razmerje med vzorcno frekvenco in pasovno sirino zaprtozancnega sistema $f_b[Hz]$ ali $\omega_b[rad^-1]$ naj bo dovolj visoko
- v literaturi najdemo razlicna priporocila
	- razmerja naj bodo npr med 6 in 40 ali 5 in 100
	- ce zelimo, da je maksimalna zakasnitev med spremembo reference __pod 10 % casa vzpona__  $t_r$
	- pri nadkriticno dusenih sistemih cas vzpona definiramo kot cas v katerem odziv naraste z 10% na 90% koncne vrednosti, pri podkriticno dusenih pa od 0% do 100%
- _Odvisnost od hitrosti zaprtozancnega odziva:_
	- privzamemo razmerje med vzorcno frekvenco in pasovno sirino ZZ odziva __Vsaj 20__ , to pomeni: $\frac{2\pi}{T_0} \geq 20 \omega_b$ oziroma $\frac{1}{T_{0}}\geq 20f_b$
	- pasovna sirina je povezana s casom vzpona $t_r$, za sistem 1. reda velja $f_{b}*t_{r} \approx 0.35$ 
	- od tu sledi $T_{0} \leq \frac{1}{20*f_b}\approx\frac{1}{20*\frac{0,35}{t_r}}$ oziroma:
	![[izbira_casa_vz.png]]
	- pri kriticno dusenem odzivu je zveza nekoliko drugacna, pri $\zeta = 0,7$ velja priblizno:
![[izbira_casa_vz_2.png]]
### Izvedba diskretnega PID algoritma z locenimi cleni P, I, D
![[loceni_cleni_pid.png]]
## Stopenjske izvedbe PID regulatorja
- Pulzni tip izhoda
	- dvostanjsi je ponavadi uporabljen v povezavi z np elektricnimi grelci![[dvostanjski_izhod_pid.png]]
	- trostanjski je ponavadi uporabljen v povezavi z elektro motornimi pogoni
![[trostanjski_izhod_pid.png]]


# Reference
# Tags
#rvp #pid #discrete #closedLoop 
