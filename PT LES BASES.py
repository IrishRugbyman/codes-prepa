import numpy as np
from math import *
import matplotlib.pyplot as plt

L_test1 = [1, 6, 4, 7, 4, -1, -4, 0, 4, 3]
L_test2 = "on assure les bases"
T_test = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.]
Y_test = [0, 0.1, 0.4, 0.9, 1.6, 2.5, 3.6, 4.9, 6.4, 8.1, 10]

def maxi(L):
    max = L[0]
    for i in L:
        if i > max:
            max = i
    return max

def indice_mini(L):
    min = L[0]
    k = 0
    for i in L:
        if i < min:
            a = k
            k = k + 1
            min = i
        else:
            k = k + 1
    return a

def  occurrence(a, L):
    k = 0
    for val in L:
        if val == a:
            k = k + 1
    return k

def points(N):
    L = []
    for i in range(N):
        L.append(N - i -1)
    return L

def trace_cercle(R, N):
    X = np.zeros(N)
    Y = np.zeros(N)
    for i in range(N):
        X[i] = R * cos(2*pi*i/N)
        Y[i] = R * sin(2*pi*i/N)
    plt.axis("equal")
    plt.plot(X,Y)
    plt.show()

def derivee_g(y,t):
    dY = []
    for i in range(1,11):
        dY.append((y[i]-y[i-1])/(t[i]-t[i-1]))
    return dY

def moyenne_glissante_5(L):
    