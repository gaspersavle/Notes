1. __Proces z omejenim vhodom [0 - Umax ] reguliramo z diskretnim PI-regulatorjem. Za čas vzorčenja izberemo T0 = 1 s. Zahtevamo, da je pri odzivu na enotino stopničasto spremembo pogreška ter pri k > 0 sprememba regulirne veličine med dvema trenutkoma vzorčenja enaka ∆umax = 0,5. Obenem naj regulirna veličina u(k) doseže maksimum umax = 10 po 8 intervalih vzorčenja od spremembe pogreška, če je bil izhod regulatorja pred spremembo pogreška enak 0. Kolikšno je proporcionalno ojačenje KP in kolikšna je integrirna časovna konstanta TI takšnega regulatorja?__

u(0) = 0
umax = u(8) = 10

$$u(k) = u(k-1) + q_{0}\cdot e(k) + q_{1} \cdot e(k-1) + q_{2}\cdot e(k-2)$$






2. __Dano je kombinacijsko krmilje, ki ga opisuje preklopna funkcija 
	Y = (nC ⋅ D + C ⋅ nD)⋅ B + nB ⋅(A⋅nC ⋅ nE + nA ⋅C ⋅ E) 
	Napišite oz. narišite dele programov, ki realizirajo dano krmilje, v vseh štirih osnovnih programskih jezikih standarda IEC 61131-3.
	- _Instruction List (IL)_
		LDN B
		AND(
		AND(
		LDN C
		AND D
		)
		OR(
		LD C
		ANDN D
		)
		)
		OR(
		LD nB
		AND (
		AND(
		LD A
		ANDN C
		ANDN E
		)
		OR (
		LDN A
		AND C
		AND E
		)
		)
		)
		ST Y
	
	- _Structured Text (ST)_
		Y = B AND (NOT C AND D OR(C AND NOT D)) OR(NOT B AND (A AND NOT C AND NOT E OR (NOT A AND C AND E)))
	- _Ladder Diagram (LD)_ 
		![[Pasted image 20230116151041.png]]
	- _Function block diagramme (FBD)_
		![[imageedit_1_5873646285.png]]



3. __Napišite program v jeziku ST (v skladu s standardom IEC 61131-3), s katerim izvedemo krmiljenje šaržnega reaktorja na sliki. Ta mora delovati v skladu z naslednjimi zahtevami:__
	- Po pritisku tipke START reaktor prične delovati. Posoda se prične vzporedno polniti s snovjo A preko ventila V_A in snovjo C preko ventila V_C
	- Polnjenje z A se zaključi, ko nivo v posodi doseže stikalo LS_A. Nato se posoda prične polniti s snovjo B preko ventila V_B, polnjenje s C pa se nadaljuje
	- Polnjenje z B se zaključi po 100 s od vklopa LS_A ali ob sklenitvi LS_B, hkrati se zaključi tudi polnjenje s C
	- Če je ob koncu polnjenja vključeno stikalo LS_B, se vključi signal ALARM, po potrditvi alarma s tipko ACK alarm ugasne, posoda pa se izprazni preko ventila V_D do razklenitve stikala LS_E
	- Če ob koncu polnjenja stikalo LS_B ni vključeno, sevključi mešanje ME in gretje GR, ki ostane vključeno 1200 s. Po poteku tega časa se posoda ob nadaljevanju mešanja izprazni preko V_E. Mešanje se izključi ob koncu, ko je posoda prazna
	- Ne glede na to, ali je bil med postopkom vključen alarm ali ne, se po koncu praznjenja postopek ponovi, ne da bi ponovno pritisnili START, razen če je bila med delovanjem pritisnjena tipka STOP
![[Pasted image 20230116140612.png]]





4. __Narišite lestvični diagram (v skladu s standardom IEC 61131-3), s katerim realiziramo prehajanje stanj v prikazanem sekvenčnem funkcijskem diagramu. Privzemite, da je za signalizacijo zagona krmilnika na voljo sistemska spremenljivka START_PLK__
![[Pasted image 20230116140546.png]]

# Tags
#izpit  #rvp #primer #izpitno2023