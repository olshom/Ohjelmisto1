class Auto():
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, nopeuden_muutos):
        if self.nopeus+nopeuden_muutos <0:
            self.nopeus = 0
        elif self.nopeus+nopeuden_muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus += nopeuden_muutos

    def kulje(self, tuntimaara):
        self.matka += tuntimaara*self.nopeus


auto = Auto('ABC-123', 142)
print(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka)
auto.kiihdytä(30)
auto.kulje(1)
print(auto.nopeus, auto.matka)
auto.kiihdytä(70)
auto.kulje(1.5)
print(auto.nopeus, auto.matka)
