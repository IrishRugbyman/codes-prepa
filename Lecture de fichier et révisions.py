import math as m
import matplotlib.pyplot as plt


def lecture(nom_fichier):
    fichier = open(nom_fichier, "r")
    lignes = fichier.readlines()
    Nlignes = len(lignes)
    temps, vitm = [], []
    for ligne in lignes[2:]:
        ligne = ligne.replace(",", ".")
        ligne = ligne.strip("\n")
        A, B = ligne.split(";")
        temps.append(float(A))
        vitm.append(float(B))
    return [temps, vitm]


tps, vit_nf = lecture(("Cordeuse.csv"))[0], lecture(("Cordeuse.csv"))[1]

plt.plot(tps, vit_nf, label="vitesse non filtrée")
plt.xlabel("Temps")
plt.ylabel("Vitesse")


def moy_glissante(M, V):
    N = len(V)
    V_ff = [0] * N
    V_f = [0] * N
    for i in range(M):
        V_f[i] = V[i]
        V_ff[i] = V[i]
    for i in range(M, N - M):
        for k in range(i - M, i + M + 1):
            V_ff[i] += V[k]
            V_f[i] = V_ff[i] / (2 * M + 1)
    return V_f


for k in [1, 4, 10, 30]:
    V_filtr = moy_glissante(k, vit_nf)
    labelplt = "vitesse filtrée avec M = " + str(k)
    plt.plot(tps, V_filtr, label=labelplt)
plt.xlabel("Temps")
plt.ylabel("Vitesse")
plt.legend(loc="upper right")

def u(t):
    if t <= 0.96:
        return 17
    elif 0.96 < t and t <= 2.55:
        return - 24
    elif 2.55 < t and t <= 2.66:
        return 24
    else:
        return 0


def eq_diff(f, R, K, J, N_pts, vit_init, tf):
    vit_init = vit_init * (2 * m.pi / 60)
    tps = [0] * N_pts
    vit = [0] * N_pts
    vit[0] = vit_init
    delta = tf / (N_pts - 1)
    K2 = (K / (J * R))
    K1 = (f + (K ** 2 / R)) / J
    for i in range(N_pts - 1):
        vit[i + 1] = vit[i] + delta * (K2 * u(delta * i) - K1 * vit[i])
        tps[i + 1] = tps[i] + delta
    return vit, tps


f = 4.2 * 10 ** (-4)
R = 1.1
K = 0.025
J = 1.7 * 10 ** (-4)
N_pts = 5000
vit_init = 3700
tf = 3.2


def fonction1(vit, tps,a,b):  # vit et tps sont deux listes de même taille
    L_vit_rech = []
    L_tps_rech = []
    for i in range(len(tps)):
        if tps[i] >= a and tps[i] <= b:
            L_vit_rech.append(vit[i])
            L_tps_rech.append(tps[i])
    return L_vit_rech, L_tps_rech


def fonction2(vit, tps):
    L_vit_rech, L_tps_rech = vit, tps
    a, b = 0, len(L_tps_rech)
    k = int((a + b) / 2)
    while a < b:
        if L_vit_rech[k] > 0:
            a = k + 1
        else:
            b = k
        k = int((a + b) / 2)
    return k


L = fonction2(moy_glissante(10, vit_nf), tps)
vit3, tps3 = moy_glissante(10, vit_nf)[L:], tps[L:]

print(tps3[0])
print(vit3[0])
plt.plot(tps3,vit3,'+')

def course(vit, tps, k, R):
    A = 0
    for i in range(0, len(vit) - 1):
        vit[i] = - vit[i]
        A = vit[i] + abs(vit[i+1] - vit[i]) / 2
        return k * R * A

R = 10
k = 1/53

print("course =",course(vit3, tps3, k, R))

plt.show()