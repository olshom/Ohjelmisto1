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


h = Hissi(2, 7)
h.siirry_kerrokseen(9)