liste = sorted(eval(input("Entrez votre liste de nombres, sans oublier les crochets: ")))
r = int(input("Entrez l'entier recherché: "))

def dichotomie(liste, r):
    g, d = 0, len(liste) - 1
    while g <= d:
        n = (g+d)//2
        if liste[n] == r:
            print("Le chiffre ",r," est présent dans le tableau ",liste)
            exit()
        if liste[n] < r:
            g = n+1
        if liste[n] > r:
            d = n-1
    print("Non, le chiffre ",r," n'est pas présent dans le tableau ",liste)

dichotomie(liste,r)

[12,18,47,68,79]