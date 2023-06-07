# 1. Histogram
_Dvo-modalen_ ima 2 vrha, en predstavlja ozadje, drug pa sam predmet
_Vec-modalen_ ima vrhove za barve

$$P_{i}= \frac{n_{i}}{n} \rightarrow \frac{stevilo\space te\space vrednosti \space v \space matriki}{stevilo \space vseh \space vrednosti \space v \space matriki}$$
P dolocamo za vsako vrednost, ki je predstavljena v histogramu
$$P^{*}_{n} = P_{0}+ P_{1}+ ... +P_n$$
## 2. Izracun informacije
$$H_{0}(t) = -\sum\limits^{t}_{i = 0}\frac{P_i}{P^{*}(t)}\cdot\log_{2}(\frac{P_i}{P^{*}(t)})$$
$$H_{1}(t) = -\sum\limits^{L-1}_{i = t+1}\frac{P_i}{1-P^{*}(t)}\cdot\log_{2}(\frac{P_i}{1-P^{*}(t)})$$
$$INFORMACIJA =H = H_{0}+H_{1}$$
$$t = max\{H(0), H(1), ..., H(L)$$

# 3. Slika
## Algoritem ZT
Dolocimo _3 zacetne tocke_
Premikamo se od leve proti desni, od zgoraj navzdol
$$Zt_{1}= vstopna \space tocka \space v \space sliko (0,0)$$
$$Zt_{2}= prva \space tocka \space obrisa$$
$$Zt_{3}= prva \space tocka \space znotraj \space obrisa$$
## Algoritem SO
Prioritete obracanja
1. najprej preverimo tocko _levo od smeri vstopa_
2. preverimo tocko _v smeri vstopa_
3. preverimo tocko _desno od smeri vstopa_
4. preverimo tocko _v nasprotni smeri vstopa_
![[Pasted image 20230122233528.png]]
Verizna koda je zaporedje gibov, ki smo jih morali narediti da se iz zacetne tocke vrnemo nazaj vanjo po obrisu

## Fourierovi koeficienti
- Ce ima samo eno frekvencno komponento, je vzorec elipsaste ali okrogle oblike
- Nizkofrekvencni vzorci so kapljicaste oblike
- Visokofrekvencni vzorci so zvezdaste oblike
$$\begin{bmatrix}cx'\\cy'\\cz'\\c\end{bmatrix}= \begin{bmatrix}-1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&\frac{1}{f}&0\end{bmatrix} \cdot \begin{bmatrix}x\\y\\z\\1 \end{bmatrix}$$
$$x' = \frac{cx'}{c} \quad \quad y' = \frac{cy'}{c}\quad \space \space z'= \frac{cz'}{c}$$
$$u = x' \cdot k_{u}\quad \quad v = y' \cdot k_v$$ Na koncu koordinatama u in v odstejemo/pristejemo polovico posamezne dimenzije ekrana, zaradi zamika med koordinatnima sistemoma
![[Pasted image 20230122235750.png]]

# 3. Znacilke
_Evklidska mera podobnosti:_
$$D_{E}= \sqrt{\sum\limits^{n}_{j = 1}(x_{1,j}-x_{2,j})^2}$$
_City block razdalja_
$$D_{CB} = \sum\limits^{n}_{j = 1} |x_{1,j}-x_{2,j}|$$
_Chebysheva razdalja_
$$D_{C} = max_{J = 1, ..., n}\{|x_{1,j}-x_{2,j}|\}$$
_Kosinusna mera podobnosti_
$$d_{C}= cos(\phi) = \frac{\sum\limits^{N}_{i = 1}x_{1,i}\cdot x_{2,i}}{\sqrt{\sum\limits^{N}_{i = 1}x_{1,i}^2}\cdot\sqrt{\sum\limits^{N}_{i = 1}x_{2,i}^2}}$$
# 4. Vecplastni perceptron
- Stevilo vhodov enako stevilu znacilk (komponent vektorja znacilk) +1
- Stevilo izhodov enako stevilu razredov
- Vecplastni perceptron ima najmanj eno skrito plast
# 5. Razvrscanje
$$Uspesnost = P_{a}= \frac{st \space pravilno \space razvrscenih}{stevilo \space vseh}$$
$$Neuspesnost = P_{e}= 1-P_a$$
$$PPV = \frac{TP}{TP+FP} = natancnost$$
$$TPR = \frac{TP}{TP+FN} = recall$$
$$F = 2\cdot \frac{TP}{2\cdot TP + FP + FN} = merilo$$

| |A1|A2|A3|
|-|-|-|-|
|D1|x|x|x|
|D2|x|x|x|
|D3|x|x|x|

| |Pozitiven|Negativen|
|-|-|-|
|Potrjen|TP = x|FP = 1|
|Zavrnjen|FN = z|TN = 2|

$$P_{c}= \sum\limits^{M}_{i = 1} \frac{D_{1}}{vsi}\cdot\frac{A_{1}}{vsi}+\frac{D_{2}}{vsi}\cdot\frac{A_{2}}{vsi}+...$$

