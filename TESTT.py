def te(mu, i0, Ne, N12, L, S, w, E):
    T = []
    for e in E:
        t = (1 / w) * atan(L * e * (1 / (S * mu * Ne * N12 * w * i0)))
        T.append(t)
    return T

plt.plot(E, te(mu, i0, Ne, N12, L, S, w, E))
plt.xlabel("Tension de sortie")
plt.ylabel("temps")

plt.title("Tension de sortie en fonction du temps")
plt.plot(T, et(mu, i0, Ne, N12, L, S, w, T))
plt.plot(T, np.linspace(5, 5, 100))
plt.xlabel("t (s)")
plt.ylabel("Ueff (V)")