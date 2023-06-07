# Komponente
- **VGAvmesnik.vhd:** vsebuje časovni generator signalov VGA z izhodnimi koordinatami (x,y) in vmesnik za periferne enote razvojne plošče: tipke in signale za LED matrike (ledm in ledcnt)
- **proc.vhd:** vsebuje 12-bitni učni procesor CPU in model programskega pomnilnika program. Procesor ima vhod rst, ki je vezan na tipko, vhod ce s katerim omejimo hitrost izvajanja programa in vhodno-izhodno vodilo (rw, dataIO, dataProc).
- **grafika.vhd:** vsebuje vzorec komponente za prikaz sličice in logiko za izhodne barve. Komponenta prikaže kvadrat na koordinatah (x1,y1) in mrežo. Preveri, kako je narejen prikaz mreže!
- **io.vhd:** je vzorec komponente za procesorski vhodno-izhodni vmesnik, ki ga je potrebno dopolniti.
# Vhodno-izhodni vmesnik
## Navodilo
Naredi model vezja io.vhd s signali: 
	- adr je 8-bitno vhodno naslovno vodilo 
	- datin je 12-bitni vhod na katerega procesor piše 
	- rw je 2-bitni kontrolni vhod 
	- tipke so 4-bitni vhodni signal
	- datout je 12-bitni izhodni register iz katerega procesor bere 
	- x1 in y1 sta 12-bitna izhodna registra
![[proc.png]]
- vNaredi logiko za nastavljanje izhodnih registrov. Registra shranita vrednost iz 12-bitnega vhoda ob uri, pogoju rw=1 in ustreznem naslovu: x1 ob adr=1 in y1 ob adr=2.
- .Dodaj vhodni izbiralnik in register. Vektor s stanjem tipk razdeli na štiri enobitne signale, ki jih pošljemo na procesor ob ustreznem naslovu, kot prikazuje tabela. Ob uri, ustreznem naslovu in pogoju rw=2 nastavi novo vrednost registra datout.
# Preizkus
- . Dodaj opis vhodno-izhodnega vmesnika v Quartusov projekt in dopolni komponente za prikaz grafike. Za prikaz kroga manjka logika, ki določa barvo glede na vsebino pomnilnika ROM.
- Prevedi sistem in preizkusi delovanje na razvojni plošči. Procesor izvaja program, ki nastavi x1 in y1, nato pa ob aktivni tipki 0 poveča x1.
- Procesor izvede 25 milijonov operacij na sekundo ob nastavitvi delilnika ure d=0, zato se ob zaznani tipki koordinata objekta spreminja prehitro. Nastavi delilnik na 10000 in poskusi delova]nje.
- Dopolni program tako, da bo ustavil prištevanje, ko pride x do vrednosti 760. Najprej preveri delovanje na simulatorju procesorja https://lniv.fe.uni-lj.si/cpu.html, nato pa še na razvojni plošči.
- **BONUS:** _Spremeni program tako, da bo bral tudi tipko 3. Ob zaznani tipki naj zmanjšuje koordinato x._


## Koda
[io.vhd](file:/home/mufa/Desktop/Quartus/graficni_sistem/io.vhd)
## Notes
- Sintaksa switch-case:
```vhdl
case adr is                --adr = vh. spremenljivka
  when "00000001" =>       --"00000001" =  pricakovana vrednost (primer)
	x1 <= datin;           --x1 <= datin = operacija ob zgornjem primeru
  when "00000010" =>
	y1 <= datin;
  when others => null;     -- else varjanta
 end case;                 -- zakljucek switch-casea
```
#switchcase 

- Sintaksa: definiranje spremenljivk:
```vhdl
entity io is
 port (
   clk : in std_logic;
   adr : in unsigned(7 downto 0);
   datin : in unsigned(11 downto 0);
   rw : in unsigned(1 downto 0);
   tipke : in unsigned(3 downto 0);
   datout : out unsigned(11 downto 0);
   x1 : out unsigned(11 downto 0);
   y1 : out unsigned(11 downto 0) );
end io;

--ime spremenljivke : in/out tip spremenljivke 
```

- ce ne damo v statement else primera se ustvari latch kar lahko moti delovanje vezja
```vhdl
if x(4 downto 0)="11111" or y(4 downto 0)="11111" then
	rgb <= "001111";
else
	rgb <= "010101";
end if;

-- obvezen else primer
```
# Tags
#vhdl #NDES #fpga #grafika
