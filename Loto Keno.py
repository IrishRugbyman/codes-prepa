lo = int(input("Nombre de numéros possibles du 1er jeu ? "))
to = int(input("Nombre de numéros gagnants du 1er jeu ? "))
lt = (lo - to)
ke = int(input("Nombre de numéros possibles du 2ème jeu ? "))
no = int(input("Nombre de numéros gagnants du 2ème jeu ? "))
kn = (ke - no)


def Cnp(a, b, c):
    def factoriel(x):
        i = 1
        f = 1
        while i <= x:
            f = int(f * i)
            i = i + 1
        return f

    res = factoriel(a) / (factoriel(c) * factoriel(b))
    return (res)


print(Cnp(lo, to, lt))
print(Cnp(ke, no, kn))

if Cnp(lo, to, lt) < Cnp(ke, no, kn):
    print("Il y a moins de combinaisons possibles au Loto")
else:
    print("Il y a moins de combinaisons possibles au Keno")
