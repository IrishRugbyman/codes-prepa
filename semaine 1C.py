

MC = ["Fevrier", "Avril", "Juin", "Septembre", "Novembre"]
ML = ["Janvier", "Mars", "Mail", "Juillet", "Aout", "Octobre", "Decembre"]
MOIS = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]

def est_bissextile(an):
    if ((an % 4 == 0) and (an % 100 != 0)) or an % 400 == 0:
        return True
    else:
        return False
    
def longueur_mois(ms,an):
    if ms == "Fevrier":
        if est_bissextile(an):
            return 29
        else:
            return 28
    elif ms == "Fevrier" or ms == "Avril" or ms == "Juin" or ms == "Septembre" or ms == "Novembre":
        return 30
    else:
        return 31
    
def valide(jr,ms,an):
    if jr <= longueur_mois(ms,an):
        return True
    else:
        return False

def nab(date1,date2):
    L = [val for val in range(date1[2]+1,date2[2])]
    k = 0
    if date1[2] == date2[2]:
        if date2[1] == "Janvier" or (date2[1] == "Fevrier" and date2[0] <= 29):
            return 0
        else:
            k = k
    if est_bissextile(date1[2]):
        if date1[1] == "Janvier" or (date1[1] == "Fevrier" and date1[0] <= 29):
            k = k + 1
        else:
            k = k
    if est_bissextile(date2[2]):
        if date2[1] == "Janvier" or (date2[1] == "Fevrier" and date2[0] <= 29):
            k = k - 1
        else:
            k = k
    for i in L:
        if est_bissextile(i):
            k += 1
        else:
            k = k
    return k

dat1 = [10, "Janvier",1904]
dat2 = [1, "Mars", 1904]
print(nab(dat1,dat2))
