# nicolas pernot

# Programme de traitement de donnees sur la consommation de petrole

# on dispose d'une matrice donnant pour n annees la consommation de petrole pour chaque mois de l'annee
# ce tableau est represente par une liste de matrices sous la forme :
# [[an0, cons_an0_mois0, cons_an0_mois1, cons_an0_mois2, ...],
#  [an1, cons_an1_mois0, cons_an1_mois1, cons_an1_mois2, ...],...]
# chaque ligne correspond a  la consommation pour une anneee


# on dispose egalement de la liste des mois

# Main
# definition de la liste des mois

lmois = ["janvier", "fevrier", "mars", "avril", "mai", "juin",
         "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]

# definition de la liste des cours du petrole 
lcours = [[2005, 44.51, 45.48, 53.17, 51.88, 48.54, 54.35, 57.52, 63.95, 62.91, 58.49, 55.24, 56.87],
          [2006, 62.99, 60.21, 62.06, 70.26, 69.64, 68.56, 73.67, 73.23, 61.96, 57.81, 58.76, 62.47],
          [2007, 53.63, 57.52, 62.05, 67.49, 67.32, 71.05, 76.82, 70.76, 76.97, 82.34, 92.51, 90.93],
          [2008, 91.99, 95.05, 103.78, 109.07, 123.15, 132.32, 133.19, 113.42, 97.7, 71.59, 52.34, 40.25],
          [2009, 43.29, 43.26, 46.54, 50.19, 57.38, 68.68, 64.46, 72.52, 67.61, 72.77, 76.65, 74.46],
          [2010, 76.17, 73.64, 78.83, 84.84, 75.31, 74.76, 75.39, 77.09, 77.77, 82.67, 85.29, 91.47],
          [2011, 96.61, 103.73, 114.64, 123.21, 114.4, 114.03, 116.75, 110.38, 112.84, 109.55, 110.61, 107.87],
          [2012, 110.68, 119.44, 125.45, 119.75, 110.17, 95.16, 102.54, 113.36, 113.05, 111.7, 109.14, 109.46]]
          

# affichage de la moyenne des cours du petrole pour chaque annee

for val in lcours:
    S = 0
    for m in range(1,13):  
        S = S + val[m]
    moy = S/12.     

    print("la moyenne du cours du petrole pour l'annee", val[0], "est de :",round(moy,2))

# recherche du cours minimum
mini = 100
for val in lcours:
    for m in range(1,13):
        cours = val[m]
        if cours<=mini:
            # j'observe un nouveau minimum
            # je conserve l'annee et le mois  
            mini = cours
            an_min = val[0]
            mois_min = m

# j'affiche le resultat
# je recherche le nom du mois dans le tuple des noms de mois

print("le cours minimum est de",mini,"observe en",lmois[mois_min-1], "de l'annee",an_min)
