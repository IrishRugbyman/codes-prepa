def notes_mat(i):
    fichier = open("Matiere_" + str(i) + ".txt", "r")
    lignes = fichier.readlines()
    Nlignes = len(lignes)
    liste_noms, liste_notes, coefficient = [], [], []
    premligne = lignes[0].strip("\n").split("\t")
    coefficient = int(premligne[-1])
    for Ligne in lignes[2:]:
        Ligne = Ligne.replace(",", ".")
        Ligne = Ligne.strip("\n")
        A, B = Ligne.split("\t")
        liste_noms.append(A)
        liste_notes.append(float(B))
    return [liste_noms, liste_notes, coefficient]


print(notes_mat(1))


def moy_class_par_matiere(matiere_i):
    notes = notes_mat(matiere_i)[1]
    somme = 0
    for i in range(len(notes)):
        somme = somme + notes[i]
    moy = somme / len(notes_mat(matiere_i)[0])
    return moy


print(moy_class_par_matiere(1))


def moy_par_candidat():
    liste_noms = notes_mat(1)[0]
    liste_moyennes = []
    moyenne = 0
    MOY = []
    for g in range(len(notes_mat(1)[0])):
        num = 0
        denom = 0
        for i in range(1, 10):
            num = num + (float(notes_mat(i)[1][g]) * float(notes_mat(i)[2]))
            denom = denom + float(notes_mat(i)[2])
        moyenne = num / denom
        MOY.append(moyenne)
    return [liste_noms, MOY]


print(moy_par_candidat())


def tri_candidats():
    Ln = moy_par_candidat()[0]
    Lm = moy_par_candidat()[1]
    for i in range(1, len(moy_par_candidat()[0])):
        for j in range(i):
            if Lm[j] > Lm[i]:
                Lm[j], Lm[i], Ln[j], Ln[i] = Lm[i], Lm[j], Ln[i], Ln[j]
    return [Lm, Ln]


print(tri_candidats())


def autres_candidats():
    fichier = open("notes_autres_candidats.txt", "r")
    lignes = fichier.readlines()
    liste_candidats, liste_notes = [], []
    for Ligne in lignes[2:]:
        Ligne = Ligne.replace(",", ".")
        Ligne = Ligne.strip("\n")
        A, B = Ligne.split("\t")
        liste_candidats.append(A)
        liste_notes.append(B)
    for i in range(len(liste_candidats)-1):
        if str(liste_notes[i]) == "NC":
            liste_notes.pop(i)
            liste_candidats.pop(i)
    return [liste_candidats, liste_notes]


print(autres_candidats())
