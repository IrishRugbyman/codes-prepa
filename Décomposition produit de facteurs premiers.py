from math import *

# Variables
n = int(input("Entrez le nombre à tester: "))
i = n - 1
listes = []
exposants = []
decomp = []
nn = n


for j in range(2, n + 1):
    i = 2
    for i in range(2, int(sqrt(n) + 1)):
        if i < j and j % i == 0:
            break
    else:
        listes.append(j)
print(listes)


while 1 < nn:
    for var in listes:
        if nn % var == 0:
            decomp.append(var)
            nn = nn / var
print(decomp)


exposants = decomp[:]
for var in exposants:
    if exposants.count(var) != 1:
        exposants.remove(var)
print(exposants)


i = 0
print("La décomposition en facteurs premiers de ", n, " est: ")
for i in range(len(exposants)):
    exp = decomp.count(exposants[i])
    print(exposants[i], " exposant ", exp)
