# 

25.11.2022
19:25
[[# Tags]]
[[# Reference]]

# Navodilo
1. funkcija __obdelaj_sliko__ ^7de942
	1. Prevzorčenje slike na velikost 256 x 256 pikslov z uporabo cv2.resize
	2. Pretvorba barvne slike v sivinsko z uporabo cv2.cvtColor
	3. Filtriranje sivinske slike z uporabo filtra mediane z okolico 11px
	4. Upragovljanje filtrirane slike s postopkom maksimizacije informacije
	5. vrni obdelano sliko
2.  funkcija __pretvori_obris_v_signal__ ^7ccd7b
	1.  Pretvorba obrisa, iz zapisa v obliki zaporedja točk v kompleksni signa
	2. izvedi pretvorbo
3.  funkcija __doloci_ffk__  ^9ef94b
	1. Izvedi izračun d_ij po formuli, podani v literaturi
	

# Povzetek
Izpeljava znacilk obrisov, program __vzame obris, ki nam ga vrne vaja 2__:
![[vaja2.py]]
![[obrisi.py]]
1. obris, ki ga prejmemo je zapisan v obliki __seznama parov tock__ (koordinate x in y), pretovriti ga moramo v __kompleksni signal__, zapisan v formatu __{X1 + jY1, ..., Xn + jYn}__
2. na kompleksnem signalu nato izvedemo fourierovo transformacijo, koeficiente diskretne fourierove informacije dobimo iz enacbe:![[izracun_koeficientov_fourierove_transformacije.png]]
__rezultat pretvorbe:__
![[rezultat_fourierove_transformacije.png]]
3. glede na dolzino vektorjev znacilk, jim dolocimo barvo, nato jih izrisemo v graf:![[izris_znacilk.png]]
4.  glede na __evklidsko razdaljo__ in __kosinusno mero podobnosti__ izrisemo graf parov vektorjev znacilk: ![[prikaz_podobnosti_vektorjev.png]]

# Izvedba
1. [[#^7de942 | Obdelaj sliko]]
```python
def obdelaj_sliko(slika):
    """Pomožna funkcija za predobdelavo slike.
    Vhod: barvna slika
    Izhod: binarna slika"""

    # 1. Prevzorčenje slike na velikost 256 x 256 pikslov z uporabo cv2.resize
    skaliranaSlika = cv2.resize(slika,[256,256])  #moja koda
    # 2. Pretvorba barvne slike v sivinsko z uporabo cv2.cvtColor
    sivaSlika = cv2.cvtColor(skaliranaSlika, cv2.COLOR_BGR2GRAY)  #moja koda
    # 2. Filtriranje sivinske slike z uporabo filtra mediane z okolico 11px
    obdelanaSlika = cv2.medianBlur(sivaSlika, 11)  #moja koda
    # 3. Upragovljanje filtrirane slike s postopkom maksimizacije informacije
    prag = dolociPrag(obdelanaSlika)  #moja koda

    _, Osama_BinSlika = cv2.threshold(obdelanaSlika, prag, 255, 0)  #moja koda
    return Osama_BinSlika
```
2. [[#^7ccd7b | Pretvori obris v signal]]
```python
def pretvori_obris_v_signal(obris):
    """Pretvorba obrisa,
    iz zapisa v obliki zaporedja točk v kompleksni signal."""
    tocke_obrisa = obris["tocke"]
    dolzina = len(tocke_obrisa)
    signal = np.zeros((dolzina,), dtype=np.complex128)
    # TODO: izvedi pretvorbo
    sledilnik = 0
    for par in tocke_obrisa:
        signal[sledilnik] = (complex(par[0], par[1]))
        sledilnik += 1
    return signal
```
3. [[#^9ef94b | Doloci FFK]]
```python
def doloci_ffk(slika, kmax, lmax):
    """Določitev vektorja značilk iz najdaljšega obrisa na sliki."""
    binarnaSlika = obdelaj_sliko(slika)

    iskalnikObrisov = Iskalnik(binarnaSlika)
    iskalnikObrisov.isci_obrise()
    obris = iskalnikObrisov.podaj_najdaljsi_obris()

    signal = pretvori_obris_v_signal(obris)
    signal = prevzorci_signal(signal)

    signal_fft = np.fft.fft(signal)

    vektor_ffk = np.zeros((2 * kmax * (lmax - 1),), dtype=np.float64)
    ind_vektor = 0

    for i in range(1, kmax + 1):
        for j in range(2, lmax + 1):
            d_ij = ((np.power(signal_fft[i+1],j))*(np.power((signal_fft[len(signal_fft)-j+1]),i)))/(np.power(signal_fft[1],(i+j)))
            d0 = d_ij.real
            d1 = d_ij.imag
            vektor_ffk[ind_vektor] = d0
            vektor_ffk[ind_vektor + 1] = d1
            ind_vektor += 2

    return vektor_ffk

```
## Težave
- graf kosinusne podobnosti se ne prikazuje pravilno, poslal mail profesorju, da mi pove kaj je narobe
- baje na kosinusno podobnost zelo vplivajo majhn,e visokofrekvencne komponente, kar lahko pomeni, da je probelm tam
- sicer kosinusna podobnost operira z istimi podatki, kot evklidska razdalja, torej ne bi smelo biti hude napake pred to operacijo
## TO - DO
- __zrihtaj kosinusno podobnost__ [[#TO - DO]]
## Notes
__ZRIHTAJ__
```python
# TODO: izračunaj kosinusno podobnost ter negativno evklidsko 
            #       razdaljo med vektorjema v1 in v2
            sest_e = 0
            sest_stevec = 0
            sest_im1 = 0
            sest_im2 = 0
            for indeks in range(len(v1)):
                sest_e += np.power((v1[indeks]-v2[indeks]),2)
                sest_stevec += (v1[indeks]*v2[indeks])
                sest_im1 += np.power(v1[indeks],2)
                sest_im2 += np.power(v2[indeks],2)    
            #print("sesetevek evkl: ", sest_e)
        
            razdalje_evk[i, j] = np.sqrt(sest_e)
            
            podobnosti_cos[i, j] = sest_stevec/(np.sqrt(sest_im1)*np.sqrt(sest_im2))
            #podobnosti_cos[i,j] = (v1@v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    #print("razdalje", razdalje_evk)
```
# Reference
1. https://e.fe.uni-lj.si/mod/resource/view.php?id=2416
2. https://e.fe.uni-lj.si/mod/page/view.php?id=15816
# Tags
#isva #znacilke #computer_vision #python #cv2 #numpy #matplotlib
