# s = n (n + 1)/2
import numpy as np

A, B, C = np.array([[4, 9, 2], [3, 5, 7], [8, 1, 6]]), np.array([[4, 9, 2], [3, 5, 7], [8, 6, 1]]), np.array(
    [[4, 9, 2], [3, 4, 7], [8, 1, 6]])


def MatriceOK(T):
    n = len(T)
    N = [i for i in range(1, (n ** 2) + 1)]
    for i in range(n):
        for j in range(n):
            if N.count(T[i][j]) == 1:
                N.remove(T[i][j])
    if N == []:
        return True
    return False


def EstMagique(T):
    n = len(T)
    s = n * (n ** 2 + 1) / 2
    if MatriceOK(T):
        for i in range(len(T)):
            h = 0
            s = 0
            l = 0
            k = 0
            for j in range(len(T)):
                s += T[i][j]
                print("s=",s)
                h += T[j][i]
                print("h=",h)
                l += T[j][j]
                print("l=",l)
                k += T[n-j-1][j]
                print("k=",k)
            if s != s or h != s or l != s or k != s:
                return False
        return True
    else:
        return False

print(EstMagique(B))