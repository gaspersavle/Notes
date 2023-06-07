from obrisi import *

import sys, os

if __name__ == "__main__":
    # Preberi sliko s podanega datotečnega imena
    try:
        filename = sys.argv[1]
    except IndexError:
        print("Uporaba programa: python vaja1a.py <datotečno ime slike>")
        sys.exit(1)

    # Branje slike in pretvorba barvnega prostora
    slika = cv2.imread(filename)
    slika = cv2.cvtColor(slika, cv2.COLOR_BGR2RGB)
    sivaSlika = cv2.cvtColor(slika, cv2.COLOR_RGB2GRAY)

    # TODO: Obdelava sivinske slike, npr. s postopki
    # izravnave histograma, filtrom mediane in Gaussovim glajenjem

    #obdelanaSlika = cv2.medianBlur(sivaSlika, 9)
    obdelanaSlika = sivaSlika

    # Izračun in prikaz histograma ter slik

    histogram = izracunajHistogram(obdelanaSlika)
    narisiHistogram(histogram)
    
    plt.figure()
    plt.title("Barvna slika")
    plt.imshow(slika)

    plt.figure()
    plt.title("Sivinska slika")
    plt.imshow(sivaSlika, cmap="gray")

    plt.figure()
    plt.title("Obdelana slika")
    plt.imshow(obdelanaSlika, cmap="gray")

    prag = dolociPrag(obdelanaSlika)
    
    _, upragovljenaSlika = cv2.threshold(obdelanaSlika, prag, 255, 0)

    print(prag)

    plt.figure()
    plt.title("Upragovljena slika")
    plt.imshow(upragovljenaSlika, cmap="gray")

    # TODO: dopolni kodo razreda obrisi.Iskalnik
    # TODO: poišči obrise v upragovljeni sliki
    # TODO: posebej izriši vse obrise naenkrat ter najdaljši obris
    # TODO: shrani najdaljši obris v besedilno datoteko,
    #       v obliki zaporedja točk

    
    iskalnikobrisov = Iskalnik(upragovljenaSlika)
    iskalnikobrisov.isci_obrise()
    print(iskalnikobrisov.podaj_najdaljsi_obris())

    
    obris_slike = narisi_obris(upragovljenaSlika,iskalnikobrisov.podaj_najdaljsi_obris(),255)
    print("risemobris")
    plt.figure()
    plt.title("najdaljsi obris")
    plt.imshow(obris_slike, cmap="gray")

    vsiobrisi = iskalnikobrisov.narisi_vse_obrise()
    plt.figure()
    plt.title("vsi obrisi")
    plt.imshow(vsiobrisi, cmap="gray")
    

    plt.show(block=False)

    with open('tocke.txt', 'w') as my_file:
        najdaljsi_obris = iskalnikobrisov.podaj_najdaljsi_obris()
        my_file.write(str(najdaljsi_obris['tocke']))

    input("Press any key.")
    plt.close("all")
    sys.exit(0)


