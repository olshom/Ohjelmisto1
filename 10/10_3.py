class Hissi:
    def __init__(self, alimman_kerros, ylimman_kerros):
        self.kerros = alimman_kerros
        self.alimman_kerros = alimman_kerros
        self.ylimman_kerros = ylimman_kerros

    def siirry_kerrokseen(self, kerros):
        kerroksen_muutos = self.kerros - kerros
        if kerroksen_muutos > 0:
            [self.kerros_alas() for _ in range(kerroksen_muutos) if self.kerros > self.alimman_kerros]
        elif kerroksen_muutos < 0:
            [self.kerros_ylös() for _ in range( -1*kerroksen_muutos) if self.kerros < self.ylimman_kerros]

    def kerros_ylös(self):
        self.kerros += 1
        print(self.kerros)

    def kerros_alas(self):
        self.kerros -= 1
        print(self.kerros)

class Talo:
    def __init__(self, alimman_kerros, ylimman_kerros, hissit):
        self.alimman_kerros = alimman_kerros
        self.ylimman_kerros = ylimman_kerros
        self.hissit = [Hissi(alimman_kerros, ylimman_kerros) for _ in range(hissit)]

    def aja_hissiä(self, hissin_numero, kohdekerros):
        self.hissit[hissin_numero-1].siirry_kerrokseen(kohdekerros)
        #print(self.hissit[hissin_numero-1].kerros, self.hissit[hissin_numero-1].kerros)

    def palohälytys(self):
        [self.aja_hissiä(numero, self.alimman_kerros) for numero in range(len(self.hissit))]


talo = Talo(2,13,3)

talo.aja_hissiä(2, 4)
talo.aja_hissiä(2, 15)
talo.aja_hissiä(1, 1)
talo.aja_hissiä(3, 5)
talo.aja_hissiä(1, 8)
talo.palohälytys()
print(talo.hissit[0].kerros)
print(talo.hissit[1].kerros)
print(talo.hissit[2].kerros)