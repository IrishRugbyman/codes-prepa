import numpy as np
from math import *
import matplotlib.pyplot as plt

def divise2(n):
    a = n%10
    if a in [0,2,4,6,8]:
        return True
    return False

def divise5(n):
    a = n % 10
    if a == 0 or a == 5:
        return True
    return False

def somme(n):
    k = str(n)
    s = 0
    for val in k:
        s = s + int(val)
    return s

def divise3(n):
    while somme(n) > 10:
        n = somme(n)
    if somme(n) in [0,3,6,9]:
        return True
    return False



def divise9(n):
    while somme(n) > 10:
        n = somme(n)
    if somme(n) in [0,9]:
        return True
    return False

def unpas(k):
    p = (k//10) - 2 * (k%10)
    return p

def divise7(n):
    while unpas(n) > 7:
        n = unpas(n)
    if n in [0,7,14,21]:
        return True
    return False

print(divise7(31976))