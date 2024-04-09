

def quedesuns(n):
    N = "1"
    if n % 5 == 0 or n % 2 ==0:
        return "Erreur"
    else:
        while int(N) % n != 0:
            N = N + "1"
    return int(N)

#i = 1
#while i < 150:
#    if i % 5 == 0 or i % 2 ==0:
#        i = i + 1
#    else:
#        print(i,quedesuns(i))
#        i = i + 1

def longueur(k):
    return len(str(k))

i = 1
lmax = 0
imax = 0
while i < 1000:
    if i % 5 == 0 or i % 2 ==0:
        i = i + 1
    else:
        if longueur(quedesuns(i)) > lmax:
            lmax,imax  = longueur(quedesuns(i)),i
        i = i + 1
    
print("Pour n =",imax,"on a N composé de",lmax,"chiffres  1")
