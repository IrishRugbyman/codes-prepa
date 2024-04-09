#Variables
d=int(input("La date du jour, sous forme d'entier à six chiffres: "))
m=0
a=0

#Calculs
a=d%100
d=d//100

m=d%100
d=d//100

print("Nous sommes le: ",d,"/",m,"/",a)


