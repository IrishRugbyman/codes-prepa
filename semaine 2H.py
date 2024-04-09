from math import sqrt

p = (3,2)
print(p[0])

def iterer(p):
    a = sqrt(p[0]*p[1])
    b = 2/(1/p[0]+1/p[1])
    return (a,b)

def suite(u,v,n):
    a,b = u,v
    p = (a,b)
    for i in range(1,n+1):
        p = iterer(p)
    return p

def moyenne(u,v):
    Lg, Ld = str(suite(u,v,1000)[0]),str(suite(u,v,1000)[1])
    L = ""
    print(Lg,Ld)
    for i in range(len(Lg)):
        while Lg[i] <= Ld[i]:
            L += (Lg[i])
            i = i + 1
            print(L)
moyenne(3,2)
