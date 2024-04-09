from math import*

#variables
d=0
p=0
a=0

#calcul
d=float(input("Entrez le diamètre du cercle en cm: "))
if d<0:
    print("Le diamètre doit être positif")
else:
    p=pi*d
    r=d/2
    a=pi*r*r
    print("Le perimêtre est de: ",p,"cm")
    print("La surface du cercle est: ",a,"cm²")
