import numpy as np

M = np.zeros([5, 5]).astype(int)
n = 5
M[0,1] = 9
M[0,2] = 3
M[0,4] = 7
M[1,2] = 1
M[1,3] = 8
M[2,3] = 4
M[2,4] = 2

for i in range(n):
    for j in range(n):
        if i < j and M[i,j] == 0:
            M[i,j] = -1

for i in range(n):
    for j in range(n):
        if i > j:
            M[i,j] = M[j,i]

L = []
for i in range(n):
    if M[4,i] != -1 and M[4,i] != 0:
        L.append(M[4,i])

def voisins(i):
    k = i
    L = []
    for i in range(n):
        if M[k, i] != -1 and M[k, i] != 0:
            L.append(M[k, i])
    return L
print(voisins(0))
def degre(i):
    return len(voisins(i))

def longueur(L):
    l = 0
    for i in range(len(L)):
        print(L[i])
        print(voisins(L[i]))
        if L[i + 1] not in voisins(L[i]):
            return -1
        else:
            l += M[i,i+1]
    return l

print(longueur([3,2]))