x = float(input("Entrez votre argent: "))
n = int(input("À décimale arrondir ? "))

def décimale_n(x, n):
    x = str(x)
    j = x[x.index(".")+1:len(x)]
    if len(j) < n:
        d=0
        return (d)
    else:
        d = x[(x.index(".")) + n+1]
        return (d)

def arrondi_pair(p):
    p = int(input("Entrez un nombre entier: "))
    if p%2==0:
        print(p)
    else:
        print(p+1)



def arrondi_bancaire(x,n):
    x = str(x)
    j = x[x.index(".")+1:len(x)]
    if len(j) < n:
        d=0
    else:
        d = x[(x.index(".")) + n+1]
    d=float(d)
    if d <= 4:
        x=float(x)
        x=x-(x % 0.01)
        print(x)
    if d==5:
        d = x[(x.index(".")) + n]
        d=float(d)
        if d % 2 == 0:
            x=float(x)
            x = x - (x % 0.01)
            print(round((x),2))
        else:
            x=float(x)
            x = x - (x % 0.01)
            print(round((x+0.01),2))
    else:
        x=float(x)
        print(round((x),2))

arrondi_bancaire(x,n)