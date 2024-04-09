cdc = str(input("Entrez votre chaîne de caractères: "))
n = int(input("Nombre de caractères maximum: "))


def filtre_ligne(n, cdc):
    m = len(cdc)
    if m <= n:
        print(cdc)
    else:
        print("Votre châine de caractères est trop longue !")


filtre_ligne(n,cdc)
