

def croissante(lili):
    for i in range(len(lili)-1):
        if lili[i] >= lili[i+1]:
            return False
    return True

def decroissante(lili):
    for i in range(len(lili)-1):
        if lili[i] <= lili[i+1]:
            return False
    return True

def monotone(lili):
    for i in range(len(lili)-1):
        if lili[i] > lili[i+1] or lili[i] < lili[i+1]:
            return False
    return True


lili = [1,2,3,4,5,7,8,9,10,10,0,1,2,-1,1,3,5,1,4,1,2,3,4,5,7,8,9,10,10]

def TC(lili,p):
    if decroissante(lili) or monotone(lili):
        return "La liste n'est pas croissante"
    else:
        for i in range(len(lili)):
            for j in range(i,len(lili)-i):
                while croissante(lili[i:j]) and j < len(lili):
                    if len(lili[i:j]) == p:
                        return [lili[i:j],i]
                    j = j + 1
        return "Pas trouvé"

def max_croissante(lili):
    if decroissante(lili) or monotone(lili):
        return "La liste n'est pas croissante"
    else:
        a,b,amax,bmax = 0,0,0,0
        for i in range(len(lili)):
            for j in range(i,len(lili)-i):
                while croissante(lili[i:j]) and j < len(lili):
                    a,b = i,j
                    j = j + 1
                if (b - a) > (bmax - amax):
                    amax,bmax = a,b
    return [lili[amax:bmax],amax]

print("La plus grande tranche croissante est", max_croissante(lili)[0],"et c'est à l'index",max_croissante(lili)[1],"de la liste testée qu'elle débute")
