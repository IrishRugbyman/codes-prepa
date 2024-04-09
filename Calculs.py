#Variables
f=int(0)
p=int(input("Entrez le premier entier: "))
d=int(input("Entrez le deuxième entier: "))
s=input("Entrez l\'opération souhaitée, sous la forme: + - / ou *: ")

#Calculs
if s=="+": 
        f=p+d
        print("Le résultat est: ",f)
elif s=="-":
        f=p-d
        print("Le résultat est: ",f)
elif s=="/":
        f=p/d
        print("Le résultat est: ",f)
else:
        f=p*d
        print("Le résultat est: ",f)

