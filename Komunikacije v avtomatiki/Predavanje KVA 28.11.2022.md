
28.11.2022
19:32
[[# Tags]]
[[# Reference]]

# Teme
- TCP socket
	- potrjevanje paketov __kumulativno/selektivno__
	- sestava TCP glave
	- three way handshake
	- TCP options
	- max velikosti paketov, RTT
- IP protokol
	- tip prenosa
	- razlike med IPv4 in IPv6
## Potrjevanje paketov
### Snov
- 2 tipa potrjevanje, __kumulativno__ in __selektivno__
	- __kumulativno:__ ko pride do napake pri prenosu paketov s TCP protokolom, prejemnik postavi zastavico __ACK__, vendar podatek __ACKN NUMBER__ postavi na serijsko stevilko zadnjega pravilno prejetega paketa, ko oddajnik zazna, da se je  __ACKN NUMBER__ spremenil v vrednost, ki se je ze zgodila se v njem postavi zastavica __DUPLICATE ACKN__, ko se ta zastavica v njem ponovi 3x, znova poslje pakete od njega dalje. Temu vedenju pravimo _Fast Retransmit_, oziroma _Hitra ponovitev_
	   ![[kumulativno_potrjevanje.png]]
	- __selektivno:__ ko pride do napake pri prenosu podatkov, TCP prejemnik ravna enako, kot pri kumulativnem potrjevanju, vendar oddajnik tokrat po _fast retransmit-u_ znova poslje le pakete, ki so bili okvarjeni, saj je prejemnik sposoben zacasno shraniti pakete, ki so se pravilno prenesli po okvarjenem
	-
### Najpomembnejse
### Formule
### Primeri

# Reference
# Tags
#kva #tcp #ip 