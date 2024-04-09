import numpy as np
from scipy import linalg

A = [[2, 2, -3], [-2, -1, -3], [6, 4, 4]]
B = [[2], [-5], [16]]


def permutation(A, i, j):
    n = len(A[0])
    for k in range(0, n):
        A[i][k], A[j][k] = A[j][k], A[i][k]
    return A


def permutation(B, i, j):
    m = len(B[0])
    for k in range(0, m):
        B[i][k], B[j][k] = B[j][k], B[i][k]
    return B


def transvection(A, B, i, j, mu):
    n = len(A[0])
    m = len(B[0])
    for k in range(0, n):
        A[i][k] = A[i][k] + mu * A[j][k]
    for k in range(0, m):
        B[i][k] = B[i][k] + mu * B[j][k]
    return A, B


def ech(A, B):
    n = len(A[0])
    m = len(B[0])
    for j in range(0, n - 1):
        ip = pivot(A, j)
        A = permutation(A, ip, j)
        B = permutation(B, ip, j)
        for i in range(j + 1, n):
            mu = (-A[i][j] / A[j][j])
            A, B = transvection(A, B, i, j, mu)
    return A, B


def pivot(A, j):
    n = len(A)
    ip = j
    pivot = A[j][j]
    while abs(pivot) == 0:
        ip = ip + 1
        pivot = A[ip][j]
    return ip


def remontee(A, B):
    n = len(A[0])
    m = len(B[0])
    X = [0 * i for i in range(n)]
    for i in range(n - 1, -1, -1):
        T = 0
        for k in range(n):
            T = T + A[i][k] * X[k]
        X[i] = ((B[i][0] - T) / A[i][i])
    return X


def Gauss(A, B):
    A, B = ech(A, B)
    X = remontee(A, B)
    return X


print("Gauss:", Gauss(A, B))
print("Linalg:", np.linalg.solve(A, B))


# Pour_améliorer_le_programme:

def pivot_partiel(A, j):
    n = len(A[0])
    ip = j
    pivot = A[j][j]
    for k in range(j + 1, n):
        if pivot < abs(A[k][j]):
            pivot = abs(A[k][j])
            ip = k
    return k
