from turtle import *

côté = 0


def carré(côté):
    côté = float(input("Entrez la longueur d'un côté de votre carré : "))
    reset()
    i = 0
    while (i < 4):
        speed(1)
        forward(100)
        right(90)
        i = i + 1


def triangle(côté):
    i = 0
    while (i < 4):
        speed(1)
        forward(100)
        left(120)
        i = i + 1


carré(côté)
triangle(côté)
