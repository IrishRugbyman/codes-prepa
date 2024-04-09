from random import *

def somme(n):
    L = list(str(n))
    s = 0
    for val in L:
        s += int(val)
    return s

def adequat(n):
    k = somme(n)
    if k % 10 == 0:
        return True
    else:
        return False

def modification(n):
    p = n
    if adequat(p):
        return p
    else:
        h = p // 10
        p = str(p)
        s = somme(h)
        while s >10:
            s -= 10
        p = str(h) + str(10 - s)        
    return int(p)

s = 0
for i in range(10000):
    K = randint(1000,100000)
    if adequat(K):
        s += 1
print(s)


        
