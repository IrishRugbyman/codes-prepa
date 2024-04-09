import random as rand
import numpy as np
import matplotlib.pyplot as plt


def vect_alea(N):
    V = np.zeros(N)
    V[0] = rand.randint(1, 4)
    for i in range(1, N):
        V[i] = (V[i - 1] + rand.randint(1, 4))
    return (V)


def element(VECT):
    a = rand.randint(0, np.size(VECT) - 1)
    return VECT[a]


def balayage(X, VECT):
    for i in range(len(VECT)):
        if VECT[i] == X:
            return i
    print("Erreur : nombre non trouvé")


def dichotomie(X, VECT):
    g = 0
    d = np.size(VECT) - 1
    compteur2 = 0
    m = int((g + d) / 2)
    while d > g:
        if VECT[m] < X:
            g = m + 1
        else:
            d = m
        m = int((g + d) / 2)
        compteur2 = compteur2 + 1
    return [m, compteur2]


def f1(vect_test, M):
    it1, it2 = 0, 0
    vect = vect_test
    r = element(vect)
    for i in range(M):
        it1 += balayage(r, vect)
        it2 += dichotomie(r, vect)[1]
    return [it1 / M, it2 / M]

def f2(Nmax, M):
    IT1,IT2 = [],[]
    for N in range(2, Nmax):
        vect = vect_alea(N)
        IT1.append(f1(vect,M)[0])
        IT2.append(f1(vect,M)[1])
    return IT1,IT2

log = np.logspace(0,250,251)
plt.loglog(log,f2(log,100)[0])
plt.loglog(log,f2(log,100)[1])
