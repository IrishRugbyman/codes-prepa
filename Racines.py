from math import*

#variables
a=0
b=0
c=0
delta=0
r1=0
r2=0

print("Il faut une expression de la forme ax²+bx+c == 0")

#demandes
a=float(input("Valeur de a: "))
b=float(input("Valeur de b: "))
c=float(input("Valeur de c: "))

#calculs
delta=b*b-4*a*c
if delta > 0:
        r1=(-b-sqrt(delta))/2*a
        r2=(-b+sqrt(delta))/2*a
        print("Les solutions de l'équation sont: ",r1," et ",r2)
elif delta == 0:
    r1=(-b)/2*a
    print("La solution de l'équation est: ",r1)
else:
    r1=(-b/(2*a))-(sqrt(-delta)/(2*a))*1j
    r2=(-b/(2*a))+(sqrt(-delta)/(2*a))*1j
    print("Les solutions de l'équation sont: ",r1," et ",r2)
