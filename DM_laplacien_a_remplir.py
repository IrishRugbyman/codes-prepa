### Espace d'appel des bibliotheques ###

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt  # ne nous servira que pour la fonction m.sqrt


# a la limite on aurait pu taper "from math import sqrt"


### Espace de definition des fonctions - et des variables locales ###

def p(i, j, N):  # cette fonction calcule la densite de charge au point M(i,j)
    if 0.25 < i < 0.75 and 0.25 < j < 0.75:  # condition traduisant le fait que le point i,j appartient au disque C
        return 2100 / (N - 1) ** 2  # voir sujet, bas de page 1
    else:  # si le point M(i,j) n'appartient pas au disque
        return 0  # voir sujet, bas de page 1


def initialisation(N):
    Table = np.zeros([N, N])  # matrice carrée de N lignes N colonnes, remplie de 0
    Table[:, 0] = np.linspace(0, 100, N)  # ici on affecte la 1ere colonne de Table avec un linspace
    Table[:, N - 1] = np.linspace(0, -100, N)  # ici on affecte la derniere colonne de Table avec un linspace
    Table[N - 1, :] = np.linspace(100, -100, N)  # et ici on affecte la derniere ligne de Table avec un linspace
    return Table



def iteration(V):
    V2 = np.copy(V)  # on copie la table V = Vk integralement
    N = len(V2)  # on recupere le nombre de lignes, ou de colonnes, de la table V
    for i in range(1, N - 2):  # attention a ne pas ecraser les conditions limites !
        for j in range(1, N - 2):
            V2[i, j] = ((p(i, j, N) + V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1])) / 4  # on construit la table Vk+1 a l'aide de la table Vk en argument
    return V2  # on renvoie la table Vk+1 calculee grace a Vk


def ecart(V2, V1):  # V2, V1 deux tables carrees de meme dimension
    N = len(V2)
    e = 0
    for i in range(1, N - 1):
        for j in range(0, N - 1):
            e += (V2[i, j] - V1[i, j]) ** 2
    e2 = sqrt(e / N ** 2)
    return e2  # moyenne quadratique de l'ecart entre V2 et V1

def resolution(N, emax):
    V0 = initialisation(N)  #
    V1 = iteration(V0) # calcul de V1
    diff = ecart(V0,V1)  # ecart moy quadratique entre V0 et V1
    liste_conv = [diff]  # liste dans laquelle on ecrira tout du long les ecarts quadratiques, pour tracer graphe de convergence
    while diff > emax :  # condition d'execution de la boucle
        V0,V1 = V1, iteration(V1)# creation
        diff = ecart(V0, V1)  # ecart quadratique moyen entre Vk et Vk-1
        liste_conv.append(diff)
    return V1, liste_conv


### Espace des variables globales, et d'appel aux fonctions ###

Npts = 30  # au dela de N = 30, je crains que vos processeurs ne saturent
L = 1e-2  # dimension de l'enceinte, imposee
ecart_max = 1e-2  # en dessous de cette valeur, le calcul prendra pas mal de temps

Vapp, ecarts = resolution(Npts,ecart_max)  # creation simultanee de Vapp (la tension approchee) et de epsilon (la liste des ecarts successifs)
V_trace = np.flip(Vapp,1)  # a Vapp remise dans "le bon sens" pour le trace

x, y = np.linspace(0, L, Npts), np.linspace(0, L, Npts)  # en metre
X, Y = np.meshgrid(x, y, indexing='ij')  # permet de faire un trace 2D
cs = plt.contourf(X, Y, V_trace, levels=np.linspace(-100, 100, 200))  # convention : valeur de potentiel = couleur
plt.xlabel("x en m")
plt.ylabel("y en m")
plt.colorbar(cs)  # affiche le code couleur
plt.show()

Kmax = ...  # nombre d'iterations de l'algorithme de resolution qui ont ete necessaires
print("Le nombre d'iterations nécessaires a été Kmax =", Kmax)
