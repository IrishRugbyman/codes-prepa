#Variables
prix=float(input("Quelle est la somme à payer ? "))
d=float(input("Combien le client a-t-il donné ? "))
p2=0
p1=0
p50=0
p20=0
p10=0
r=0

#Calculs
r=d-prix

p2=r//2
r=r%2

p1=r//1
r=r%1

p50=r//0.50
r=r%0.50

p20=r//0.20
r=r%0.20

p10=r//0.10
r=r%0.10

print("Il faut rendre: ",p2," pièces de 2, ",p1," pièces de 1, ",p50," pièces de 0.50, ",p20," pièces de 0.20, ",p10," pièces de 0.10")
