#Variables
j=int(input("Combien de jours souhaitez vous garder le véhicule ? "))
d=float(input("Combien de km allez vous parcourir avec le véhicule ? "))
p1=0
p2=0
p3=0
p4=0

#Calculs
p4=(25*j)
p4=p4+(0.2*p4)

if d<100:
    p1=d*0.4
    p1=p1+(0.2*p1)+5*j
    if p1<p4:
        print("Vous devez payer ",p1)
    else: print("Vous devez payer ",p4)

elif 100<d<1000:
    p2=d*0.3
    p2=p2+(0.2*p2)+5*j
    if p2<p4:
        print("Vous devez payer ",p2)
    else: print("Vous devez payer ",p4)


else:
    p3=0.1*d
    p3=p3+(0.2*p2)+5*j
    if p3<p4:
        print("Vous devez payer ",p3)
    else: print("Vous devez payer ",p4)
    



