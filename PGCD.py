# Variables
a = int(input("Entrez le premier nombre: "))
b = int(input("Entrez le deuxième nombre, différent de 0: "))
r = 0
i = a

while 2<=i:
    if a % b == 0:
        print("Le PGCD est", b)
        exit()
    else:
        a, b = b, a % b
        i = i - 1
print("Les deux nombres sont premiers entre eux")
