from math import log

def binaire(n):
    L = []
    i = n
    if n == 0:
        return [0]
    while i != 1:
        L.insert(0,i % 2)
        i = i // 2
    L.insert(0,1)
    return L

def NombreDeUns(n):
    L = binaire(n)
    un = L.count(1)
    return(un)

def palin_2(n):
    L = binaire(n)
    k = len(L)
    for i in range(k//2):
        if L[i] != L[-i-1]:
            return False   
    return True

def listepalin(n):
    for i in range(n+1):
        if palin_2(i) == True:
            print(i,"est un 2-palindrome:",binaire(i))
        else:
            i = i

def baseB(n,b):
    L = []
    i = n
    if n == 0:
        return [0]
    while i != 1:
        L.insert(0,i % b)
        i = i // b
    L.insert(0,1)
    return L

def palinB(n,b):
    L = baseB(n,b)
    k = len(L)
    for i in range(k//2):
        if L[i] != L[-i-1]:
            return False   
    return True

L = []
i = 0
while len(L) <= 10:
    if palinB(i,4) and palinB(i,9):
        L.append(i)
        print(i)
    i = i + 1
print(L)
