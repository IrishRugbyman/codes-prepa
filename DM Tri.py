import time
import random

L = [random.randint(1, 1000) for i in range(5000)]


def tri_selection(L):
    start = time.time()
    L_a_trier = L[:]
    L_triee = []
    while L_a_trier != []:
        indice_element_mini = 0
        for i in range(len(L_a_trier)):
            if L_a_trier[i] < L_a_trier[indice_element_mini]:
                indice_element_mini = i
        L_triee.append(L_a_trier.pop(indice_element_mini))
    return time.time() - start


print("Pour 5000 valeurs aléatoires: \n"
      "- Le tri par sélection nous renvoie une liste triée en", tri_selection(L), "secondes")


def tri_selection_en_place(L):
    for i in range(len(L)):
        indice_element_mini = i
        for j in range(i + 1, len(L)):
            if L[j] < L[indice_element_mini]:
                indice_element_mini = j
        L.insert(i, L.pop(indice_element_mini))


def tri_insertion(L):
    start = time.time()
    for i in range(1, len(L)):
        for j in range(i):
            if L[j] > L[i]:
                L[j], L[i] = L[i], L[j]
    return time.time() - start


print("- Le tri par insertion nous renvoie une liste triée en", tri_insertion(L), "secondes")


def tri_insert_en_place(L):
    for i in range(1, len(L)):
        for j in range(i - 1, len(L)):
            if L[j] < L[j - 1]:
                L[j], L[j - 1] = L[j - 1], L[j]


def fusion(L1, L2):
    L = []
    N = max(len(L1), len(L2))
    for i in range(N - 1):
        if L1[0] < L2[0]:
            L.append(L1.pop(0))
        else:
            L.append(L2.pop(0))
    L = L + L1 + L2
    return L


def decoupe(L):
    L1 = []
    for i in range(int(len(L) / 2)):
        L1.append(L.pop(0))
    L2 = L[:]
    return L1, L2


def tri_fusion(L):
    if len(L) <= 1:
        return L
    else:
        L1, L2 = découpe(L)
        return fusion(tri_fusion(L1), tri_fusion(L2))


def timefusion(L):
    t2 = time.time()
    tri_fusion(L)
    return time.time() - t2


print("- Le tri par fusion nous renvoie une liste triée en", timefusion(L), "secondes")


def partition(L):
    G, D = [], []
    piv = L.pop(len(L) - 1)
    for val in L:
        if val < piv:
            G.append(val)
        else:
            D.append(val)
    return [piv], G, D


def tri_rapide(L):
    if len(L) <= 1:
        return L
    else:
        piv, G, D = partition(L)
        return tri_rapide(G) + piv + tri_rapide(D)


def timerapide(L):
    t1 = time.time()
    tri_rapide(L)
    return time.time() - t1


print("- Le tri rapide nous renvoie une liste triée en", timerapide(L), "secondes")
