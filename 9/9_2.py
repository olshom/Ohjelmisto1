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

auto = Auto('ABC-123', 142)
print(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka)
auto.kiihdytä(30)
print(auto.nopeus)
auto.kiihdytä(70)
print(auto.nopeus)
auto.kiihdytä(50)
print(auto.nopeus)
auto.kiihdytä(-200)
print(auto.nopeus)