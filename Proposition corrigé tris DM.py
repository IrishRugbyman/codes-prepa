import random as rd

def tri_selection(L, test = False) :
    L2 = L.copy()
    Lsort = []
    compteur = 0 # A Supprimer pour timer
    while len(L2) > 0 :
        indice_min_L2 = 0
        for j in range(len(L2)) :
            if L2[j] < L2[indice_min_L2] :
                indice_min_L2 = j
            compteur += 1 # A Supprimer pour timer
        Lsort.append(L2[indice_min_L2])
        del L2[indice_min_L2]
    if test :
        return compteur # A Supprimer pour timer
    return Lsort
 
def tri_selection_en_place(L) :
    for i in range(len(L)-1) :
        indice_mini = i
        for j in range(i+1, len(L)) :
            if L[j] < L[indice_mini] :
                indice_mini = j
        L[i], L[indice_mini] = L[indice_mini], L[i]
 
    
def tri_insertion(L, test = False) :
    L2 = L.copy()  # pas necessaire si procedural
    compteur = 0 # A Supprimer pour timer
    for i in range(1,len(L)) :
        for j in range(i) :
            if L2[i]<L2[j] :
                L2.insert(j,L2[i])
                del L2[i+1] # i+1 car il a été décalé à droite par l'insertion
            compteur += 1
    if test :
        return compteur # A Supprimer pour timer
    return L2   # pas necessaire si procedural

def tri_insertion_en_place(L):
    for i in range(1,len(L)) :
        j = i
        while L[j] < L[j-1] and j > 0 :
            L[j] , L[j-1] = L[j-1], L[j]
            j -= 1


def fusion(L1, L2) : #L1 et L2 sont 2 listes triées
    global compteur1
    LA = L1.copy()
    LB = L2.copy()
    Lsort = []
    while len(LA) != 0 and len(LB) != 0 :
        if LA[0] > LB[0] :
            Lsort.append(LB[0])
            del LB[0]
        else :
            Lsort.append(LA[0])
            del LA[0]
        compteur1 += 1
    Lsort = Lsort + LA + LB # on rajoute les derniers elements
    return Lsort

def decoupe(L):
    global compteur1
    compteur1 += 1
    if len(L) > 1 :
        return L[:len(L)//2], L[len(L)//2:]
    else :
        return L, []

def tri_fusion(L) :
    L2 = L.copy()
    if len(L2) > 1 : # ou >= 2
                    # on arrete donc la recursivite avec des [] et des [...] (0 ou 1 élément)
        G, D = decoupe(L2) #gauche, droite
        return fusion( tri_fusion(G), tri_fusion(D)) # recursivite
    else :
        return L2

def partition(L) : # découpage par rapport au dernier element
        # on va ranger tous les L[i] < L[k] a gauche de k
        # et tous les L[i] > L[k] a droite de k
    global compteur2
    pivot = L[-1]
    G = []
    D = []
    for i in range(len(L)-1) : # g est exclu puisque pivot
        if L[i] < pivot :
            G.append(L[i])
        else  :
            D.append(L[i])
        compteur2 += 1
    return G, pivot, D        
    

def tri_rapide(L) :
    L2 = L.copy()
    if len(L2) > 1 : # ou >= 2
                    # on arrete donc la recursivite avec des [] et des [...] (0 ou 1 élément)
        Gauche, Piv, Droite = partition(L) #gauche, droite
        return tri_rapide(Gauche) + [Piv] + tri_rapide(Droite)
    else :
        return L2

def recherche(L, k) : # je cherche la valeur qui serait a la position k dans L triée
    G, Piv, D = partition(L)
    if len(G) == k  :
        return Piv
    elif len(G) < k : # on cherche a droite
        #G.append(Piv)
        return recherche(D, k - len(G) - 1)
    else : # on cherche a gauche
        #D.append(Piv)
        return recherche(G,k)
        
    


def partition2(L, g, d) : # découpage par rapport au dernier element
        # on va ranger tous les L[i] < L[k] a gauche de k
        # et tous les L[i] > L[k] a droite de k
    global compteur2
    pivot = L[d] # valeur pivot = le dernier élément
    i = g # position finale du pivot
    for j in range(g, d) : # d est exclu puisque pivot
        if L[j] <= pivot :
            L[i], L[j] = L[j], L[i]
            i += 1
        compteur2 += 1
    L[i], L[d] = L[d], L[i]
    return i        
    

def tri_rapide2(L, deb, fin) : 
    if deb < fin :
        index = partition2(L,deb,fin)
        tri_rapide2(L,deb, index-1) # la demi liste de gauche
        tri_rapide2(L,index+1, fin) # la demi liste de droite
    
    
    
def selection2(L,deb,fin,rang): # renvoie la position qu'aurait l'element de rang donné dans une liste triée
    # a chaque iteration on divise pour mieux reigner    
    # if deb==fin: # ca c'est en cas d'erreur
    #    return liste[deb]
    i = partition2(L,deb,fin) # on decoupe L en deux, L[j<i] < L[i] < L[j>i]
    # k = i-deb+1 # decalage d'indice, k est le 1er indice de la sous liste L[deb<=j<i] < L[i] < L[i<j<=fin]
    if i == rang: # on a trouve k tel que k = rang cherche
        return L[i] # on renvoie la valeur associee
    elif i > rang : # i > r donc l'element cherche se trouve dans la sous-liste de gauche L[deb<=j<i] < L[i]
        return selection2(L,deb,i-1,rang)
    else: # i < r donc l'element cherche se trouve dans la sous-liste de droite L[i] < L[i<j<=fin]
        return selection2(L,i+1,fin,rang)


compteur1 = 0 # pour comprendre la recursivite tri fusion  
compteur2 = 0 # pour comprendre la recursivite tri rapide

"""
N_tst = 1000 # nombre de points de la liste aléatoire a trier
N_stats = 100 # nombre de points sur laquelle est faite la moyenne

moy_selection = 0
moy_insertion = 0
moy_fusion = 0
moy_quicksort = 0
moy_mediane_rap = 0


for i in range(N_stats) :
    L = [rd.randint(-N_tst, N_tst) for i in range(N_tst)]
    moy_selection += tri_selection(L, True)/N_stats
    moy_insertion += tri_insertion(L, True)/N_stats
    compteur1 = 0
    tri_fusion(L)
    moy_fusion += compteur1/N_stats
    compteur2 = 0
    tri_rapide(L)
    moy_quicksort += compteur2/N_stats
    compteur2 = 0
    a = selection2(L,0,N_tst-1,N_tst//2)
    moy_mediane_rap += compteur2/N_stats # mediane = rang N/2 valeur entiere
    b = recherche(L,N_tst//2)

    
print("en moyenne sur 100 essais avec 1000 pts, nous avons")
print(moy_selection, " iterations par tri selection")
print(moy_insertion, " itérations par tri insertion")
print(moy_fusion, " itérations par tri fusion")
print(moy_quicksort, " itérations par tri rapide")
print(moy_mediane_rap, " itérations par recherche rapide")
"""