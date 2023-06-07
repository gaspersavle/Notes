
# Prednosti
## Prednosti pred navadnim CNN
- CNN modeli so na podlagi strojnega vida industrijski standard, vendar imajo problem z modeliranjem eksplicitnih sirokih relacij na slikah zaradi lokalnosti uporabe kernela za konvolucijske operacije
- CNN modeli imajo slabse generalizacijske lastnosti, kot transformerji. Zato boljse generalizacijske sposobnosti dosezemo z uporabo mehanizma __self - attention__
## Prednosti pred navadnim transformerjem
- Transformerji so bili zasnovani za predvidevanje znotraj sekvenc podatkov (primarna uporaba v procesiranju naravnega jezika) 
- Transformerji vhodne podatke tretirajo kot enodimenzionalna zaporedja in se osrodotocajo ekskluzivno na modeliranje globalnega konteksta med vhodnimi podatki, kar rezultira v __znacilkah nizke resolucije__, ki imajo pomanjkanje detajlirane lokalne informacije, ki je ne moremo pridobiti nazaj z upsamplingom.
- Ta slabost vodi v nenatancno segmentacijo (stopnicaste robove, slabo prileganje...)
_Z uporabo konvolucije in transformerja lahko zdruzimo prednosti obojih:_
- CNN zmorejo detajlirano ekstrakcijo znacilk na zelo lokaliziranem nivoju
- Informacija, ki jo dobimo iz CNN lahko zelo pripomore segmentaciji s transformerjem, ki ji manjkajo prav taki detajli
# Metoda
## 1. Transformer, kot kodirnik
### 1.1 Sekvencializacija slik.
- Na bazi https://arxiv.org/abs/2010.11929 moramo najprej izvesti _tokenizacijo_
	- Vhod __X__ preoblikujemo v serijo sploscenih 2D segmentov, kjer je vsak dimenzije $P \cdot P$ pikslov, stevilo teh segmentov pa je: $$N = \frac{H\cdot W}{P^2}$$ kjer H in W predstavljata visino in sirino izvorne slike
### 1.2 Vgrajevanje segmentov
- Vektorizirane segmente __$X_i$__ "zavijemo" v D-dimenzionalni seznam, ki mu na konec pripnemo parameter lokacije, ki se ga model lahko nauci. S tem ohranimo informacijo o polozaju posameznega segmenta
$$z_{0}= [x^{1}_{p}\cdot E; \space x^{2}_{p}E;\space ...\space x^{N}_{p}\cdot E\space]+E_{pos}$$
kjer je $E_{pos}$ vektor dimenzij N x D, ki hrani pozicijske info posameznega segmenta

- Teansformerski kodirnik sestoji iz L plasti _Multihead Self-Attention (MSA)_ in _Multi-Layer perceptron (MLP)_ blokov. Posledicno je izhod L-te plasti mozno napisati v obliki:
	- $Z_{l}^{`}= MSA(LN(Z_{l}-1))+Z_{l-1}$
	- $Z_{l}= MLP(LN(Z_{l}^{`}))+Z_{l}^{`}$
- Kjer LN pomeni normalizacijski operator, $Z_l$ pa kodirano reprezentacijo slike
![[Pasted image 20230307131619.png]]
## 2. TransUNet
- Za segmentacijsko rabo modela je intuitivna resitev enostaven upscaling kodiranih reprezentacij znacilk $Z_L$ na polno resolucijo za predvidevanje gostega izhoda. 
- Za ponovno vzpostavitev prostorskega reda moramo najprej _preoblikovati velikost kodirane znacilke_, z oblike: $\frac{H\cdot W}{P^2}$ v obliko: $\frac{H}{P} \cdot \frac{W}{P}$
- Za zmanjsanje velikosti kanalov preoblikovane znacilke uporabljamo konvolucijo z velikostjo kernela 1x1
- Ta metoda ni idealna, saj je $\frac{H}{P}$ ali $\frac{W}{P}$ navadno precej manjsi od originalne locljivosti HxW, torej neizgibno rezultira v izgubi detajlov (oblike in meje objekta), ki jih pri segmentaciji nujno potrebujemo  
- Za izgubo resolucije kompenziramo z uporabo hibridne CNN-Transformer arhitekture
### 2.1 CNN-Transformer kot kodirnik
- TransUNet namesto [[#1. Transformer, kot kodirnik | cistega transformerja]] uporablja hibridni model CNN-Transformer, kjer najprej uporabimo CNN za ekstrakcijo znacilk
- Rezultat CNN ekstrakcije je v obliki 1x1 segmentov, na teh podatkih nato naredimo [[#1.2 Vgrajevanje segmentov | vgrajevanje segmentov]] 
	- Ta arhitektura nam omogoca uporabo visokolocljivostnih map znacilk pri dekodiranju
### 2.2 Kaskadni upsampling
- Vpeljemo kaskadni upsampler (CUP), ki sestoji iz vecih korakov upsamplinga za dekodiranje skritih znacilk, ki jih bomo uporabili za koncno segmentacijsko masko
- Po preoblikovanju skitih znacilk $Z_{l}\in \mathbb{R}^{\frac{H\cdot W}{P^{2}}\cdot W}$ v $\frac{H}{P} \cdot \frac{W}{P}\cdot D$ naredimo instanco CUP s kaskado vecih _upsampling blokov_, kjer vsak blok sestoji iz 2x upsampling operatorja, 3x3 konvolucijske plasti in ReLU aktivacijske plasti zaporedno
- Vidimo, da ta model rezultira v arhitekturi v obliki crke U, ki nam omogoca agregacijo znacilk na razlicnih locljivostih z uporabo skip-povezav