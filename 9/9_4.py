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


autot = [Auto(f"ABC-{number}", random.randint(100, 200) ) for number in range(1, 11)]
tulos = []
def ajaa(auto):
    tuntimaara = 0
    while True:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        tuntimaara += 1
        if auto.matka >= 10000:
            tulos.append({'auto':auto.rekisteritunnus, 'tuntimaara':tuntimaara, 'matka':auto.matka})
            break

[ajaa(auto) for auto in autot]
sorted_tulos = sorted(tulos, key=lambda tulos: tulos['tuntimaara'])

for tulos in sorted_tulos:
    print(f"{tulos['auto']} {tulos['tuntimaara']} tuntiä {tulos['matka']} km")
