import numpy as np
import matplotlib.pyplot as plt

K = 1
E0 = 4  # échelon de consigne
w0 = 10  # rad/s
y0 = 0  # CI nulles
tf = 10  # secondes
V0 = 0  # car c'est un 2nd ordre → tangente nulle à l’origine
N = 1000  # nombre de points pour Euler
t = np.linspace(0, tf, N)  # vecteur (array) des différents temps 𝑡𝑖 (0≤𝑖≤𝑁−1)
ksi_table = np.logspace(-1, 1, 500)


def y_calc(K, ksi, w0, E0, dt, y_prime, y_seconde):
    return (1 / (1 + 2 * ksi * w0 * dt + (w0 * dt) ** 2)) * (
            K * E0 * (w0 * dt) ** 2 + 2 * y_prime * (1 + ksi * w0 * dt) - y_seconde)


def eq_diff(K, ksi, w0, E0, t, y0, V0):
    dt = t[1] - t[0]
    N = np.size(t)
    t_cut = [t[i] for i in range(N - 2)]
    y = np.zeros(N)
    y[0] = y0
    y[1] = y0 + V0 * dt
    for i in range(2, N - 2):
        y[i] = y_calc(K, ksi, w0, E0, dt, y[i - 1], y[i - 2])
    return y


# for i in (0.7,0.68):
#    labelplt = "vitesse filtrée avec ξ = " + str(i)
#    plt.plot(t, eq_diff(K, i, w0, E0, t, y0, V0), label=labelplt)
# plt.legend(loc="upper right")


def trx(y, t, x, yf):
    N = np.size(t)
    ymax = yf + yf * (x / 100)
    ymin = yf - yf * (x / 100)
    tmin = t[0]
    tmax = t[0]
    for i in range(1, N):
        if y[i] > ymin and y[i - 1] < ymin:
            tmin = t[i]
        if y[i] < ymax and y[i - 1] > ymax:
            tmax = t[i]
    return max(tmin, tmax)


def abaque(ksi_table, x, K, w0, E0, t, y0, V0):
    tr = []
    for i in range(len(ksi_table)):
        trw = trx(eq_diff(K, ksi_table[i], w0, E0, t, y0, V0), t, x, 4) * w0
        tr.append(trw)
    return tr

plt.loglog(ksi_table, abaque(ksi_table, 10, K, w0, E0, t, y0, V0))
plt.show()