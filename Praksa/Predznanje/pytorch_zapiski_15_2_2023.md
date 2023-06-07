
``` python
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(torch.__version__)

```

```
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "1.13.1+cu116\n"
 }
]
```

```python
pizdumater = torch.tensor(7)
pizdumater
```

```json
[
 {
  "data": {
   "text/plain": "tensor(7)"
  },
  "execution_count": 2,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```python
jebemtimater = torch.tensor([7,7])
```

```python
jebemtimater
```

```json
[
 {
  "data": {
   "text/plain": "tensor([7, 7])"
  },
  "execution_count": 4,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```python
jebemtimater.shape
```

```json
[
 {
  "data": {
   "text/plain": "torch.Size([2])"
  },
  "execution_count": 5,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```python
jebemtimater.ndim
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "1"
  },
  "execution_count": 6,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```python
PUSIKURAC = torch.tensor([[6,9],
                          [4,2]])
PUSIKURAC
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([[6, 9],\n        [4, 2]])"
  },
  "execution_count": 7,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```python
PUSIKURAC.ndim
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "2"
  },
  "execution_count": 8,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```


```python
### Random tensor
PIZDATIMATERINA = torch.rand(5,3,4)
PIZDATIMATERINA
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([[[0.4648, 0.0866, 0.0822, 0.7782],\n         [0.1391, 0.4556, 0.9455, 0.1014],\n         [0.5837, 0.5230, 0.7540, 0.6235]],\n\n        [[0.8276, 0.9541, 0.6711, 0.4583],\n         [0.9347, 0.9484, 0.1440, 0.2995],\n         [0.1813, 0.7755, 0.9842, 0.2781]],\n\n        [[0.4326, 0.2642, 0.2758, 0.6816],\n         [0.9329, 0.9117, 0.1824, 0.5170],\n         [0.3456, 0.7610, 0.4057, 0.4402]],\n\n        [[0.0423, 0.6220, 0.4703, 0.5158],\n         [0.4126, 0.5455, 0.3125, 0.0789],\n         [0.5630, 0.8849, 0.8955, 0.3842]],\n\n        [[0.4562, 0.7745, 0.5831, 0.1740],\n         [0.4121, 0.4517, 0.3382, 0.6196],\n         [0.4856, 0.2580, 0.7054, 0.6138]]])"
  },
  "execution_count": 14,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```


```python
PIZDATIMATERINA.ndim
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "3"
  },
  "execution_count": 15,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```


```python
nule = torch.zeros(3,4)
```


```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([[0., 0., 0., 0.],\n        [0., 0., 0., 0.],\n        [0., 0., 0., 0.]])"
  },
  "execution_count": 17,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
enke = torch.ones(3,4)
```

```{.python .input}
enke

```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([[1., 1., 1., 1.],\n        [1., 1., 1., 1.],\n        [1., 1., 1., 1.]])"
  },
  "execution_count": 20,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
enke.dtype
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "torch.float32"
  },
  "execution_count": 21,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
razpon = torch.arange(0,1000, 33)
```

```{.python .input}
razpon
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([  0,  33,  66,  99, 132, 165, 198, 231, 264, 297, 330, 363, 396, 429,\n        462, 495, 528, 561, 594, 627, 660, 693, 726, 759, 792, 825, 858, 891,\n        924, 957, 990])"
  },
  "execution_count": 23,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
razpon.shape
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "torch.Size([31])"
  },
  "execution_count": 24,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
kopija = torch.zeros_like(razpon)
```

```{.python .input}
kopija
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\n        0, 0, 0, 0, 0, 0, 0])"
  },
  "execution_count": 26,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
if (kopija.shape == razpon.shape):
  print("vazi clan")
```

```{.json .output n=None}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "vazi clan\n"
 }
]
```

```{.python .input}
datatype_tensor = torch.tensor([3, 8, 9], dtype = torch.int32)
datatype_tensor.dtype
datatype_tensor
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([3, 8, 9], dtype=torch.int32)"
  },
  "execution_count": 38,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
tensor = torch.tensor([1,2,3])
tensor += 10
tensor

```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([11, 12, 13])"
  },
  "execution_count": 5,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
tensor *10


```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([110, 120, 130])"
  },
  "execution_count": 7,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
torch.mul(tensor,tensor)

```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([121, 144, 169])"
  },
  "execution_count": 8,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

### Mnozenje matrik

1. najpogostejsa operacija s tensorji
2. poznamo 2 tipa mnozenja matrik
  - Po elementih
  - Pravo matricno mnozenje

```{.python .input}
### Mnozenje po elementih
print(tensor, "*", tensor)
print(f"Equals: {tensor*tensor}")
```

```{.json .output n=None}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "tensor([11, 12, 13]) * tensor([11, 12, 13])\nEquals: tensor([121, 144, 169])\n"
 }
]
```

```{.python .input}
### Matricno mnozenje (pravo)

print(tensor, "\cdot", tensor)
print(f"Equals: {torch.matmul(tensor, tensor)}")
```

```{.json .output n=None}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "tensor([11, 12, 13]) \\cdot tensor([11, 12, 13])\nEquals: 434\n"
 }
]
```

### Najpogostejsa napaka pri matricnem mnozenju
 1. notranje dimenzije se morajo ujemati, stevilo stolpcev prve matrike mora
biti enako stevilu vrstic druge


```{.python .input}
tensor1 = torch.rand(3,2)
tensor2 = torch.rand(2,3)

```

```{.python .input}
tensor1
tensor2
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([[0.6519, 0.2240, 0.7804],\n        [0.5998, 0.7393, 0.6788]])"
  },
  "execution_count": 4,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
torch.matmul(tensor1,tensor1)
```

```{.json .output n=None}
[
 {
  "ename": "RuntimeError",
  "evalue": "ignored",
  "output_type": "error",
  "traceback": [
   "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
   "\u001b[0;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
   "\u001b[0;32m<ipython-input-5-0a9e8be194d5>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtorch\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmatmul\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtensor1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtensor1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
   "\u001b[0;31mRuntimeError\u001b[0m: mat1 and mat2 shapes cannot be multiplied (3x2 and 3x2)"
  ]
 }
]
```

```{.python .input}
torch.matmul(tensor1, tensor2)
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([[0.9686, 0.6404, 1.1368],\n        [0.5877, 0.6349, 0.6716],\n        [0.8676, 0.7139, 1.0080]])"
  },
  "execution_count": 6,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}
torch.matmul(tensor2, tensor1)
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "tensor([[1.1359, 1.1664],\n        [1.1034, 1.4756]])"
  },
  "execution_count": 7,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

### Kot vidimo lahko mnozimo le matrike, katerih dimenzije ustrezajo pravilu

### Najpogostejsa napaka pri mnozenju matrik

```
tensor_a = torch.tensor([[1,2],
[3,4]

```{.python .input}
tensor_a = torch.tensor([[1,2],
                         [3,4],
                         [5,6]])
tensor_b = torch.tensor([[7,10],
                         [8,11],
                         [9,12]])

torch.matmul(tensor_a, tensor_b)


```

```{.json .output n=None}
[
 {
  "ename": "RuntimeError",
  "evalue": "ignored",
  "output_type": "error",
  "traceback": [
   "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
   "\u001b[0;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
   "\u001b[0;32m<ipython-input-7-2ac354af25ba>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      6\u001b[0m                          [9,12]])\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 8\u001b[0;31m \u001b[0mtorch\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmatmul\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtensor_a\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtensor_b\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
   "\u001b[0;31mRuntimeError\u001b[0m: mat1 and mat2 shapes cannot be multiplied (3x2 and 3x2)"
  ]
 }
]
```

```{.python .input}
tensor_a.shape, tensor_b.shape
```

```{.json .output n=None}
[
 {
  "data": {
   "text/plain": "(torch.Size([3, 2]), torch.Size([3, 2]))"
  },
  "execution_count": 8,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}

```

### Napako velikosti lahko odpravimo s transponacijo ene izmed matrik

```{.python .input}
print(tensor_b)
print(tensor_b.T)
```

```{.json .output n=None}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "tensor([[ 7, 10],\n        [ 8, 11],\n        [ 9, 12]])\ntensor([[ 7,  8,  9],\n        [10, 11, 12]])\n"
 }
]
```

```{.python .input}
print(tensor_b.shape)
print(tensor_b.T.shape)
```

```{.json .output n=None}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "torch.Size([3, 2])\ntorch.Size([2, 3])\n"
 }
]
```

### S transponacijo smo odpravili napako neujemanja velikosti matrik

```{.python .input}
print("Originalna oblika tensor_b: \n", tensor_b, "\n", tensor_b.shape)
print("Transponirana oblika tensor_b \n:", tensor_b.T, "\n", tensor_b.T.shape)



print("Rezultat: \n", torch.mm(tensor_a, tensor_b.T))
```

```{.json .output n=None}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "Originalna oblika tensor_b: \n tensor([[ 7, 10],\n        [ 8, 11],\n        [ 9, 12]]) \n torch.Size([3, 2])\nTransponirana oblika tensor_b \n: tensor([[ 7,  8,  9],\n        [10, 11, 12]]) \n torch.Size([2, 3])\nRezultat: \n tensor([[ 27,  30,  33],\n        [ 61,  68,  75],\n        [ 95, 106, 117]])\n"
 }
]
```

# Iskanje dolocenih lastnosti tensorjev
- Min
- Max
- Sum
- ...

```{.python .input}
x = torch. arange(0, 100, 10)

min = torch.min(x)

max = torch. max(x)

mean = torch.mean(x.type(torch.float32))

print(x,"\n", "min = ",min ,"\n", "max= ", max, "\n", "mean = ", mean)
```

```{.json .output n=None}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "tensor([ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) \n min =  tensor(0) \n max=  tensor(90) \n mean =  tensor(45.)\n"
 }
]
```

# Iskanje lokacij zgoraj omenjenih lastnosti tensorjev
- argmin
- argmax

```{.python .input}
x_pos = torch. arange(0, 100, 10)

pos_min = torch.argmin(x)

pos_max = torch. argmax(x)


print(x,"\n", "min = ",pos_min ,"\n", "max= ", pos_max)
```

```{.json .output n=None}
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "tensor([ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) \n min =  tensor(0) \n max=  tensor(9)\n"
 }
]
```

# Obdelava tensorjev, preoblikovanje, stiskanje, raztezanje

- __Preoblikovanje__ - preoblikuje vhodni tensor v podano obliko
- __Predogled__ - navidez spremeni obliko tensorja za ogledovanje, vendar ga v
spominu ohrani v originalni obliki
- __Zlaganje__ - vec tensorjev kombinira, tako, da jih zlaga enega na drugega
ali anega ob drugega
- __Stiskanje__ - odstrani navidezno dimenzijo "1" iz tensorja

```tensor.shape = (1,3,2)   -_> tensor.shape = (3,2)```
- __Raztezanje__ - doda navidezno dimenzijo "1"

```tensor.shape = (3,2)   -_> tensor.shape = (1,3,2)```

- __Permutacija__ - tensor prikaze z dimanzijami _permutiranimi_ na dolocen
nacin

```{.python .input  n=41}
import torch

tenny = torch.arange(1., 10.)
tenny, tenny.shape
```

```{.json .output n=41}
[
 {
  "data": {
   "text/plain": "(tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.]), torch.Size([9]))"
  },
  "execution_count": 41,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=42}
tenny_preoblikovan = tenny.reshape(9,1)
tenny_preoblikovan, tenny_preoblikovan.shape
```

```{.json .output n=42}
[
 {
  "data": {
   "text/plain": "(tensor([[1.],\n         [2.],\n         [3.],\n         [4.],\n         [5.],\n         [6.],\n         [7.],\n         [8.],\n         [9.]]), torch.Size([9, 1]))"
  },
  "execution_count": 42,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=43}
# Predogled
z = tenny.view(1,9)
z, z.shape
```

```{.json .output n=43}
[
 {
  "data": {
   "text/plain": "(tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.]]), torch.Size([1, 9]))"
  },
  "execution_count": 43,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=44}
# view je bejsikli pointer za python plebe

```

```{.python .input  n=47}
#Zlaganje
zlozen_tenny = torch.stack([tenny,tenny,tenny,tenny],dim = 1)
zlozen_tenny, zlozen_tenny.shape
```


```json
[
 {
  "data": {
   "text/plain": "(tensor([[1., 1., 1., 1.],\n         [2., 2., 2., 2.],\n         [3., 3., 3., 3.],\n         [4., 4., 4., 4.],\n         [5., 5., 5., 5.],\n         [6., 6., 6., 6.],\n         [7., 7., 7., 7.],\n         [8., 8., 8., 8.],\n         [9., 9., 9., 9.]]), torch.Size([9, 4]))"
  },
  "execution_count": 47,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=48}
zlozen_tenny1 = torch.stack([tenny,tenny,tenny,tenny],dim = 0)
zlozen_tenny1, zlozen_tenny1.shape
```


```json
[
 {
  "data": {
   "text/plain": "(tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.],\n         [1., 2., 3., 4., 5., 6., 7., 8., 9.],\n         [1., 2., 3., 4., 5., 6., 7., 8., 9.],\n         [1., 2., 3., 4., 5., 6., 7., 8., 9.]]), torch.Size([4, 9]))"
  },
  "execution_count": 48,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=51}
#Stiskanje
print("Originalen tensor: ", tenny_preoblikovan)

stisnjen_tenny = torch.squeeze(tenny_preoblikovan)
print("Originalna oblika: ", tenny_preoblikovan.shape)
print("Stisnjena oblika: ", stisnjen_tenny.shape)
stisnjen_tenny

```


```json
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "Originalen tensor:  tensor([[1.],\n        [2.],\n        [3.],\n        [4.],\n        [5.],\n        [6.],\n        [7.],\n        [8.],\n        [9.]])\nOriginalna oblika:  torch.Size([9, 1])\nStisnjena oblika:  torch.Size([9])\n"
 },
 {
  "data": {
   "text/plain": "tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.])"
  },
  "execution_count": 51,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=55}
#Raztezanje
raztegnjen_tenny = stisnjen_tenny.unsqueeze(dim = 0)
# Argument dim nam definira na kateri dimenziji (hierarhicno) dodamo navidezno dimrnzijo "1"
print("Stisnjen tensor: ", stisnjen_tenny)
print("Stisnjena oblika: ", stisnjen_tenny.shape)
print("Raztegnjena oblika: ", raztegnjen_tenny.shape)
raztegnjen_tenny

```


```json
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "Stisnjen tensor:  tensor([1., 2., 3., 4., 5., 6., 7., 8., 9.])\nStisnjena oblika:  torch.Size([9])\nRaztegnjena oblika:  torch.Size([1, 9])\n"
 },
 {
  "data": {
   "text/plain": "tensor([[1., 2., 3., 4., 5., 6., 7., 8., 9.]])"
  },
  "execution_count": 55,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

_Vidimo da smo pridobili dodatno dimenzijo na specificirani dimenziji, v
izhodnem tensorju imamo zato se en oglati oklepaj vec_

```{.python .input  n=56}
#Permutacija
#Najprej ustvarimo nov tensor z aplikacijo iz resnicnega sveta
original = torch.rand([224,224,3])
permutiran = original.permute(2,0,1)
print("Originalna oblika: ", original.shape)
print("Permutirana oblika: ", permutiran.shape)
```


```json
[
 {
  "name": "stdout",
  "output_type": "stream",
  "text": "Originalna oblika:  torch.Size([224, 224, 3])\nPermutirana oblika:  torch.Size([3, 224, 224])\n"
 }
]
```

_V praksi se uporablja za analizo slik format:_
``` shape = [224, 224, 3]```

_Kar pomeni:_
``` shape = [visina, sirina, barvni_kanal]```


# Indeksiranje tensorjev
- sintakticno podobno numpyju

```{.python .input  n=57}
x = torch.arange(1,10).reshape(1,3,3)
x, x.shape
```


```json
[
 {
  "data": {
   "text/plain": "(tensor([[[1, 2, 3],\n          [4, 5, 6],\n          [7, 8, 9]]]), torch.Size([1, 3, 3]))"
  },
  "execution_count": 57,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=58}
x[0]
```


```json
[
 {
  "data": {
   "text/plain": "tensor([[1, 2, 3],\n        [4, 5, 6],\n        [7, 8, 9]])"
  },
  "execution_count": 58,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=59}
x[0,0]
```


```json
[
 {
  "data": {
   "text/plain": "tensor([1, 2, 3])"
  },
  "execution_count": 59,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=60}
x[0,0,0]
```


```json
[
 {
  "data": {
   "text/plain": "tensor(1)"
  },
  "execution_count": 60,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=61}
x[0,2,2]
```


```json
[
 {
  "data": {
   "text/plain": "tensor(9)"
  },
  "execution_count": 61,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=62}
# Da dobimo vse elemente nekemdimenzije uporabimo ":"
x[:, 0]
```


```json
[
 {
  "data": {
   "text/plain": "tensor([[1, 2, 3]])"
  },
  "execution_count": 62,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=63}
x[:, :, :]
```


```json
[
 {
  "data": {
   "text/plain": "tensor([[[1, 2, 3],\n         [4, 5, 6],\n         [7, 8, 9]]])"
  },
  "execution_count": 63,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=64}
x[:, :, 1]
```


```json
[
 {
  "data": {
   "text/plain": "tensor([[2, 5, 8]])"
  },
  "execution_count": 64,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=65}
x[0,0,:]
```

```json
[
 {
  "data": {
   "text/plain": "tensor([1, 2, 3])"
  },
  "execution_count": 65,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input  n=67}
x[:,:,2]
```

```json
[
 {
  "data": {
   "text/plain": "tensor([[3, 6, 9]])"
  },
  "execution_count": 67,
  "metadata": {},
  "output_type": "execute_result"
 }
]
```

```{.python .input}

```
