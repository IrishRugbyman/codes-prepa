from math import *
import matplotlib.pyplot as plt

n = int(input("Entrez n: "))
t = int(input("Entrez t: "))
T = int(input("Entrez T: "))


def S(t, n, T):
    toto = 0
    for i in range(1, n + 1):
        toto = toto + (1 / (2 * i - 1)) * sin((2 * (2 * i - 1) * pi * t) / T)
        totototal = (4 / pi) * toto
        return totototal


print(S(t, n, T))
plt.plot(S(t, n, T))
plt.show()
