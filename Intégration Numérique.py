import matplotlib.pyplot as plt
from math import *

a = float(input("Entrez a :"))
b = float(input("Entrez b: "))
n = int(input("Entrez la valeur d'un entier pair n: "))


def fonction(x):
    y = (sin(x)) ** 3
    return y


def simpson(a, b, n):
    s1 = 0
    s2 = 0
    for i in range(1, int(n / 2) + 1):
        s1 = s1 + fonction(a + (2 * i - 1) * ((b - a) / n))
    for i in range(1, int((n / 2) - 1) + 1):
        s2 = s2 + fonction(a + 2 * i * ((b - a) / n))
    sf = (3 / 2) * (((b - a) / (3 * n)) * (fonction(a) + fonction(b) + 4 * s1 + 2 * s2))
    print(sf)
    return sf


plt.plot(simpson(a, b, n))
plt.show()
