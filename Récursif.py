def facto(n):
    i, f = 1, 1
    while i < n + 1:
        f = f * i
        i = i + 1
    return f


def facto_r(n):
    if n == 1:
        return 1
    else:
        return facto_r(n - 1) * n


def puiss(x, k):
    i = 1
    p = x
    while i < k:
        p = p * x
        i = i + 1
    return p


def puiss_r(x, k):
    if k == 0:
        return 1
    else:
        return puiss_r(x, k - 1) * x


L_tst = [1, 3, 4, 6, 7, 9, 0, 1, 3, 4, 6, 1, 6]


def occurr_pile(a, L):
    copieL = L[:]
    i, compteur = 0, 0
    while i < len(L):
        if copieL.pop(0) == a:
            compteur = compteur + 1
            i = i + 1
        else:
            i = i + 1
    return compteur


def occurr_pile_r(a, L):
    if L == []:
        return 0
    elif L.pop(0) == a:
        print(L)
        return occurr_pile_r(a, L) + 1
    else:
        return occurr_pile_r(a, L)


L_test = [1, 3, 4, 6]


def somme_elements_r(L):
    if L == []:
        return 0
    else:
        return L.pop(0) + somme_elements_r(L)

def somme_elements(L):
    copieL = L[:]
    i, somme = 0, 0
    while i < len(L):
        somme = somme + copieL.pop(0)
        i = i + 1
    return somme


print(somme_elements(L_test))
