a = 1
b = 2
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return (x ** 2) - 2


def df(x):
    return (2 * x)


def dichotomie(f, a, b, eps):
    c = 0
    while abs(b - a) > eps:
        m = (a + b) / 2
        c = c + 1
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return ["x = ", m, ", Itérations = ", c, ", f(x) = ", f(m)]


def newton_residu(f, df, u0, eps):
    u = 2
    c = 0
    while abs(f(u)) > eps:
        u = u - (f(u) / df(u))
        c = c + 1
    return ["x = ", u, ", Itérations = ", c, ", f(x) = ", f(u)]


def newton_increment(f, df, u0, eps):
    u = 2
    up = u + (2 * eps)
    c = 0
    while abs(u - up) > eps:
        up = u
        u = u - (f(u) / df(u))
        c = c + 1
        return ["x = ", u, ", Itérations = ", c, ", f(x) = ", f(u)]


for i in range(1, 10):
    eps = 10 ** (-i)
    a = 1
    b = 2
    u0 = b
    print("eps = ", 10 ** (-i))
    print("Dichotomie: ", dichotomie(f, a, b, 10 ** (-i)))
    print("Résidu: ", newton_residu(f, df, u0, 10 ** (-i)))
    print("Incrément: ", newton_increment(f, df, u0, 10 ** (-i)))


# Bug vis-à-vis de fsolve que je n'ai pas réussi à résoudre donc je l'ai enlevé. On constate que Newton converge beaucup plus vite vers la valeur recherchée.

def dichotomie_bis(f, a, b, n):
    a = 1
    b = 2
    for i in range(0, n):
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        return m


def newton_bis(f, df, u0, n):
    u = u0
    for i in range(0, n):
        up = u
        u = u - (f(u) / df(u))
    return u


def erreur(f, a, b):
    erreur_dicho = []
    erreur_newton = []
    X = []
    for i in range(1, 15):
        erreur_dicho.append(abs(dichotomie_bis(f, a, b, i) - sqrt(2)))
        erreur_newton.append(abs(newton_bis(f, a, b, i) - sqrt(2)))
        X.append(i)
    print(erreur_dicho)
    print(erreur_newton)
    plt.subplot(2, 3, 1)
    plt.plot(X, erreur_dicho, 'purple', X, erreur_newton, "green")


erreur(1, 2)


def dicho_graphe(f, a, b, eps):
    abis = a
    bbis = b
    t = []
    n = 0
    while abs(b - a) > eps:
        m = (a + b) / 2
        t.append(m)
        n = n + 1
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    nn = np.zeros(len(t))
    X = np.linspace(abis, bbis, 100)
    Y = [f(x) for x in X]
    plt.subplot(2, 3, 2)
    plt.plot(X, Y, "blue", t, nn, "red")


dicho_graphe(f, a, b, eps)


def newton_graphe(f, df, u0, eps):
    u = u0
    up = u0 - 2 * eps
    n = 0
    X = [u0]
    Y = [0]
    while abs(u - up) > eps:
        up = u
        X.append(u)
        Y.append(f(u))
        u = u - (f(u) / df(u))
        n = n + 1
        X.append(u)
        Y.append(0)
