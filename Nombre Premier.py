from math import *

# Variables
n = int(input("Entrez le nombre à tester: "))
i = n - 1

while abs(sqrt(n)) <= i:
    if n % i == 0:
        print(n, " n'est pas premier")
        exit()
    else:
        i = i - 1
print(n," est premier")

