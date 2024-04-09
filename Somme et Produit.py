# Variables
l1 = int(input("Entrez le nombre de lignes de la 1ère matrice: "))
c1 = int(input("Entrez le nombre de colonnes de la 1ère matrice: "))
v1 = eval(input("Entrez la valeur initiale de chaque élément de la 1ère matrice: "))
l2 = int(input("Entrez le nombre de lignes de la 2ème matrice: "))
c2 = int(input("Entrez le nombre de colonnes de la 2ème matrice: "))
v2 = eval(input("Entrez la valeur initiale de chaque élément de la 2ème matrice: "))


# Créer une matrice
def intMatrice(l1, c1, v1):
    return [[v1] * c1 for i in range(l1)]


print(intMatrice(l1, c1, v1))


# Somme de deux matrices
def sommeMatrice(l1, c1, v1, l2, c2, v2):
    S = 0
    liste1 = 0
    if c1 < c2:
        liste1 = [v1 + v2] * c1
        for i in range((l2 - l1)):
            liste1.append(v2)
        S = [liste1 for i in range(l1)] + [[v2] * (c2) for i in range(l2 - l1)]
    else:
        liste1 = [v1 + v2] * c2
        for i in range((l1 - l2)):
            liste1.append(v1)
        S = [liste1 for i in range(l2)] + [[v1] * (c1) for i in range(l1 - l2)]
    return S


print(sommeMatrice(l1, c1, v1, l2, c2, v2))


# Produit de deux matrices (on a des matrices carrées de taille identique)
def produitMatrice(l1, c1, v1, l2, c2, v2):
    P = [[2 * (v1 * v2)] * c1 for i in range(l1)]
    return P


print(produitMatrice(l1, c1, v1, l2, c2, v2))
