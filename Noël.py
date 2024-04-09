from scipy.optimize import minimize


def trace():
    fichier = open("banc_helice.txt", "r")
    fichier.readline(1)
    fichier.readline(2)
    lignes = fichier.readlines()
    Nlignes = len(lignes)
    U, I, omeg = [], [], []
    for Ligne in lignes[2:]:
        Ligne = Ligne.replace(",", ".")
        Ligne = Ligne.strip("\n")
        A, B, C = Ligne.split(";")
        U.append(float(A))
        I.append(float(B))
        omeg.append(float(C))
    return [U, I, omeg]


def droite():
    fichier = open("Droite_ax_plus_b.csv", "r")
    LX, LY = [], []
    fichier.readline()
    fichier.readline()
    for i in range(2, 32):
        Ligne = fichier.readline()
        Ligne = Ligne.replace(",", ".")
        Ligne = Ligne.strip("\n")
        A, B, C, D, E = Ligne.split(";")
        LX.append(float(D))
        LY.append(float(E))
    return [LX, LY]


def ecart(X, Y, a, b):
    MS = 0
    for i in range(len(X)):
        y = a * X[i] + b
        MS += (y - Y[i]) ** 2
    MSE = MS / len(X)
    return MSE


def ecart_1parametre(parametres_a_et_b):  # on se ramène à 1 seule variable
    global LX, LY  # l’optimisation se fait à nuage de points constant
    # seulent varient les paramètres a et b de la droite
    a, b = parametres_a_et_b  # on extraie les paramètres d’entrée
    return ecart(droite()[0], droite()[1], a, b)  # on exécute la fonction à plusieurs arguments


a_guess = float(input("À l'oeil, donner l'ordre de grandeur de a : "))
b_guess = float(input("À l'oeil, donner l'ordre de grandeur de b : "))
# car une méthode du gradient part toujours d’un point initial pour converger
# vers le minimum local « le plus proche »
fit_scipy = minimize(ecart_1parametre, [a_guess, b_guess])  # méthode du gradient
print("Par minimisation (méthode du gradient) on trouve : ", fit_scipy.x)


def coeffs_N2(X, Y):
    Xs, Ys = 0, 0
    Xsc = 0
    XY = 0
    for i in range(len(X)):
        Xs += X[i]
        Ys += Y[i]
        Xsc += (X[i] ** 2)
        XY += X[i] * Y[i]
    Xmoy = Xs / len(X)
    Xcmoy = Xsc / len(X)
    Ymoy = Ys / len(Y)
    XYmoy = XY / len(X)
    a0 = (XYmoy - Xmoy * Ymoy) / (Xcmoy - Xmoy ** 2)
    b0 = Ymoy - a0 * Xmoy
    return [a0,b0]
print(coeffs_N2(droite()[0], droite()[1]))