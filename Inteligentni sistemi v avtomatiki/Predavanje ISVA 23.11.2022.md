
23.11.2022
19:49
[[# Tags]]
[[# Reference]]

# Teme
- Perspektivna projekcija
	- ena izmed preslikav centralno - projekcijskega modela

## Perspektivna projekcija
### Zanimivosti
- blank
### Najpomembnejse
- uporabna za opis centralno projekcijskega modela kamere
![[centralno_projekcijski_model_kamere.png]]
### Formule
- x', y', z'  => osi koordinatnega sistema __senzorja__
- x, y, z => osi koordinatnega sistema __okolja__
- f => __goriscna razdalja__
- __zveze med koordinatnima sistemoma:__
![[zveze_med_koord_sist.png]]
![[zveze_med_koord_sistemoma_1.png]]
- ti enacbi sta __nelinearni__ , zato privzemamo __homogen__ koordinatni sistem %%vse enacbe so linearne in jih lahko zapisemo v matricni obliki%%
- v homogenem koordinatnem sistemy so koordinarte __tocke T__ enake:
	__(x,y,z,1)
- njrene projekcije na senzor pa:
	__(cx', cy', cz', c)__ , kjer je __c != 0__, na splosno poljubna konstanta
- __homogena matrika P:__
![[homogena_matrika.png]]
- kartezicne koordinate tocke __T(x,y,z)__ oziroma __t(x', y', z')__ pridobimo iz koordinate __(Xh', Yh', Zh')__
   z njimi pridobimo koordinate homogenega koord sistema iz spodnjih zvez:
   ![[zveze_med_homogenim_koord_sistemom_in_projekcijo.png]]

### Primeri
blank

## Preslikave zvezne slike v digitalno sliko
### Zanimivosti
### Najpomembnejse
- za digitalne slike se vrednosti osi koordinatnega sistema podaja v pikslih namesto v milimetrih
- uvedemo skalirna faktorja __Ku > 0__ in __Kv > 0__ , ki ju navadno doloci proizvajalec kamere v __(Px/mm)__ in z zvezo:
  ![[px_per_mm.png]]
  kjer sta koordinati __u__ in __v__ podani v __pikslih__
  
### Formule
- zveza med osmi projekcije v milimetrih in pisklih: [[px_per_mm.png]]
- Preslikava tock iz metricne slikovne ravnine na menetricen senzor:
![[preslikava_metricno_v_nemetricno.png]]

### Primeri

# Reference
# Tags
#isva #preslikave #digitalna_slika #perspektivna_projekcija
