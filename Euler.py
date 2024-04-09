from math import *
import matplotlib.pyplot as plt
import numpy as np


def expo(t):
    return exp(t)


def fct(y, t):
    return y


def euler(a, b, n, yo):
    t = [0 * x for x in range(n)]
    y = [0 * x for x in range(n)]
    h = (b - a) / n
    t[0] = a
    y[0] = yo
    for i in range(n - 1):
        t[i + 1] = t[i] + h
        y[i + 1] = y[i] + h * fct(y[i], t[i])
    return [t, y]


X = np.linspace(0, 1, 100)
Y = [expo(t) for t in X]
n = [2, 4, 8, 16]
plt.title("methode euler")
for z in range(len(n)):
    plt.subplot(3, 10, z + 1)
    R = euler(0, 1, n[z], 1)
    plt.title(" euler")
    plt.plot(X, Y, "b", R[0], R[1], "r")


def HEUN(a, b, n, yo):
    t = [0 * x for x in range(n)]
    y = [0 * x for x in range(n)]
    h = (b - a) / n
    t[0] = a
    y[0] = yo
    for i in range(n - 1):
        t[i + 1] = t[i] + h
        y[i + 1] = y[i] + h / 2 * (fct(y[i], t[i]) + fct(y[i] + h * fct(y[i], t[i]), t[i + 1]))
    return [t, y]


X = np.linspace(0, 1, 100)
Y = [expo(t) for t in X]
nn = [3, 5, 10]
for z in range(len(nn)):
    plt.subplot(3, 10, z + 6)
    R = HEUN(0, 1, nn[z], 1)
    plt.title("HEUN")
    plt.plot(X, Y, "b", R[0], R[1], "r")


def HEUN(a, b, n, yo):
    t = [0 * x for x in range(n)]
    y = [0 * x for x in range(n)]
    aa = [0 * x for x in range(n)]
    bb = [0 * x for x in range(n)]
    j = [0 * x for x in range(n)]
    h = (b - a) / n
    t[0] = a
    y[0] = yo
    for i in range(n - 1):
        t[i + 1] = t[i] + h
        aa[i] = y[i] + h / 2 * fct(y[i], t[i])
        bb[i] = y[i] + h / 2 * fct(aa[i], t[i] + (h / 2))
        j[i] = y[i] + h * fct(bb[i], t[i] + (h / 2))
        y[i + 1] = y[i] + (h / 6) * (
                    fct(y[i], t[i]) + 2 * fct(aa[i], t[i] + (h / 2)) + 2 * fct(bb[i], t[i] + (h / 2)) + fct(j[i],
                                                                                                            t[i + 1]))
    return [t, y]


X = np.linspace(0, 1, 100)
Y = [expo(t) for t in X]
nnn = [3, 5, 10]
for z in range(len(nnn)):
    plt.subplot(3, 10, z + 14)
    R = HEUN(0, 1, nnn[z], 1)
    plt.title("RK4")
    plt.plot(X, Y, "b", R[0], R[1], "r")
plt.show()
print("")
print("RK4>HEUN>EULER")

h = [1 * 10 ** -1, 1 * 10 ** -2, 1 * 10 ** -3]
erreurEuler = [1, 25 * 10 ** -1, 1, 35 * 10 ** -2, 1, 36 * 10 ** -3]
erreurHeun = [4.20 * 10 ** -3, 4.50 * 10 ** -2, 4.53 * 10 ** -3]
erreurRK4 = [2.08 * 10 ** -6, 2.25 * 10 ** -10, 2.26 * 10 ** -14]

fichier = open("R2B.txt", "w")
fichier.write("EULER\n-------------------\n")
fichier.write('|{:>8s}|{:>8s}|\n'.format('h', 'erreur'))
for i in range(3):
    fichier.write('|{:>.2e}|{:>.2e}|\n'.format(h[i], erreurEuler[i]))
fichier.write("------------------\n")

fichier.write("HEUN\n------------------\n")
fichier.write('|{:>8s}|{:>8s}|\n'.format('h', "erreur"))
for i in range(3):
    fichier.write('|{:>.2e}|{:>.2e}|\n'.format(h[i], erreurHeun[i]))
fichier.write("------------------\n")

fichier.write("RK4\n------------------\n")
fichier.write('|{:>8s}|{:>8s}|\n'.format('h', 'erreur'))
for i in range(3):
    fichier.write('|{:>.2e}|{:>.2e}|\n'.format(h[i], erreurRK4[i]))
fichier.write("------------------\n")
fichier.close()
o = open("R2B.txt", "r")
print(o)
