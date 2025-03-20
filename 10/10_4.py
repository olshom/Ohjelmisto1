import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeuden_muutos):
        if self.nopeus + nopeuden_muutos < 0:
            self.nopeus = 0
        elif self.nopeus + nopeuden_muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus += nopeuden_muutos

    def kulje(self, tuntimaara):
        self.matka += tuntimaara * self.nopeus


autot = [Auto(f"ABC-{number}", random.randint(100, 200)) for number in range(1, 11)]


class Kilpailu:
    def __init__(self, nimi, kilometrit, autot):
        self.nimi = nimi
        self.kilometrit = kilometrit
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f"{auto.rekisteritunnus} {auto.matka} km")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.kilometrit:
                return True
        return False


k = Kilpailu('Suuri romuralli', 8000, autot)
tuntimaara = 0
while k.kilpailu_ohi() is False:
    k.tunti_kuluu()
    tuntimaara += 1
    if tuntimaara % 10 == 0:
        k.tulosta_tilanne()
print(f"{tuntimaara} tunnit")
k.tulosta_tilanne()
