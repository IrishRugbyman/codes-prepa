capacite = 5
L = [1, 2, 3, 4, 5]


def LIFO(L, val, depil):
    global capacite
    if depil:
        val_sortie = L[0]
        del L[0]
        return val_sortie
    elif len(L) < capacite:
        L.insert(0, val)
        return L
    else:
        val_sortie = L[0]
        del L[0]
        L.insert(0, val)
        return L


def FIFO(L, val, depil):
    global capacite
    if depil:
        val_sortie = L[- 1]
        del L[- 1]
        return val_sortie
    elif len(L) < capacite:
        L.insert(0, val)
    else:
        val_sortie = L[- 1]
        del L[- 1]
        L.insert(0, val)


def permut_circ(L, n):
    for i in range(n):
        FIFO(L, FIFO(L, True), False)
    return L


L1 = [1, 2, 3, 4, 5]
L2 = [4, 5, 6, 1, 2]


def echange_listes(L1,L2):
    for i in L1:
        FIFO(L1, FIFO(L2,0, depil = True), False)
        FIFO(L2, FIFO(L1,0,depil = True), False)
    print(L1, L2)


echange_listes(L1, L2)


def depiler_jusqua(L, v_cherchee):
    i = L[0]
    while i != (v_cherchee):
        del L1[i]
    return L
