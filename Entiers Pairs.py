# Variables
p = 0
entiers = [p]
n = int(input("Combien de nopbres voulez vous tester ? "))
i = 1

# Calculs
while i <= n:
    if i % 2 == 0:
        entiers.append(i)
        i = i + 1
    else:
        i = i + 1
print(entiers)
