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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)


s = Sähköauto('ABC-15', 180, 52.5)
p = Polttomoottoriauto('ACD-123', 165, 32.3)

s.nopeus = 75
p.nopeus = 80
s.kulje(3)
p.kulje(3)
print(f'{s.rekisteritunnus} {s.matka} km')
print(f'{p.rekisteritunnus} {p.matka} km')
