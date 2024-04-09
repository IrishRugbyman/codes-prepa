from math import*

#Variables
H=float(input("Quelle est la hauteur de l'échantillon en cm: "))
D=float(input("Quel est le diamètre de l'échantillon en cm: "))
C=float(input("Quelle est la charge du perméamètre en cm: "))
P=float(input("Quel est le poids de l'eau en g: "))
T=float(input("Durant combien de temps, en secondes ? "))
deb=0
v=0
i=0
k=0

#Calculs
deb=P/T
v=deb/(pi*(D/2)*(D/2))
i=C/H
k=v/i

print("Le coefficient de permabilité est donc de: ",k)

