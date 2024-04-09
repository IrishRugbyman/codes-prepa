import matplotlib.pyplot as plt
import numpy as np


CRUTEM = open('CRUTEM.4.2.0.0.anomalies.txt', 'r')
file_content = CRUTEM.readlines()



def get_data(y,m):
    data = []
    numligne = (y - 1850) * 12 * 37 + (m - 1) * 37 + 1
    for i in range(36):
        data.append(file_content[numligne + i])
    return data


def moyenne(x):
    l = []
    data_matrix = []
    s = 0
    z = 0
    for ligne in x:
        data_matrix.append(ligne.split())
    for j in range(72):
        for i in range(36):
            l.append(data_matrix[i][j])
    for var in l:
        if var != "-1.000e+30":
            s = s + float(var)
            z = z + 1
    if z == 0:
        return (None)
    else:
        return (s / z)


def temp_mensuel():
    mois = []
    moy = 0
    for a in range(1850, 2013):
        for m in range(1, 13):
            d = []
            d = get_data(a, m)
            moy = moyenne(d)
            mois.append(moy)
    return (mois)


def temp_annuel():
    moy = 0
    année = []
    for annee in range(1850, 2013):
        moy = 0
        for mois in range(1, 13):
            d = []
            d = get_data(annee,mois)
            moy = moyenne(d) + moy
        année.append(moy / 12)
    return (année)

def temp_décennie():
    moy = 0
    liste_decennie = []
    dec = 0
    for annee in range(11, 164):
        moy = 0
        for dec in range(annee - 11, annee - 1):
            moy = moy + y[dec]
        liste_decennie.append(moy / 10)
    return liste_decennie


Y = temp_mensuel()
X = np.linspace(1, 1956, 1956)
tabm = plt.figure()
plt.title("Anomalies Mensuelles")
plt.xlabel("Mois")
plt.ylabel("Degrés")
plt.plot(X,Y)
tabm.savefig('temp mensuel.pdf', format='pdf')

y = temp_annuel()
x = np.linspace(1850, 2013, 163)
taba = plt.figure()
plt.title("Anomalies Annuelles")
plt.xlabel("Années")
plt.ylabel("Degrés")
plt.plot(x, y)
taba.savefig('temp annuel.pdf', format='pdf')

D = temp_décennie()
d = np.linspace(1860, 2013, 153)
tabd = plt.figure()
plt.title("Anomalies Décénnie")
plt.xlabel("Décénnie")
plt.ylabel("Degrés")
plt.plot(d, D)
tabd.savefig('temp decennie.pdf', format='pdf')

plt.show()