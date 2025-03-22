class Julkaisu:
    def __init__(self,nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(self.nimi, end=' ')

class Kirje(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"(kirjailija {self.kirjoittaja}, {self.sivumäärä} sivua)")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"(päätoimittaja {self.päätoimittaja})")



lehti = Lehti('Aku Ankka', 'Aki Hyyppä')
lehti.tulosta_tiedot()
kirje = Kirje('Hytti n:o 6', 'Rosa Liksom', 200)
kirje.tulosta_tiedot()


