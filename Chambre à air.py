from math import *
import matplotlib.pyplot as plt

n = eval(input("Entrez le nombre d'intervalles: "))
d = float(input("Entrez le temps total: "))
ti = []
posX = []
posY = []


def x(n, d):
    posX = []
    i = 0
    for i in range(n):
        x = (i * (d / n)) - sin((i * (d / n)))
        posX.append(x)
    return posX


def y(n, d):
    posY = []
    i = 0
    for i in range(n):
        y = 1 - cos((i * (d / n)))
        posY.append(y)
    return posY


def posinstx(t):
    xt = t - sin(t)
    return xt


def posinty(t):
    yt = 1 - cos(t)
    return yt

def vx(t):
    vitessex = []
    i=0
    for i in range(n):
        vitessex.append((posintx(t + (d/n)) - posintx(t - (d/n)))/2*(d/n))
    return vitessex

def vy(t):
    vitessey = []
    i=0
    for i in range(n):
        vitessey.append((posinty(t + (d/n)) - posinty(t - (d/n)))/2*(d/n))
    return vitessey

positionX = x(n, d)
positionY = y(n, d)
plt.subplot(3,1,2)
plt.show(t,vitessey)


