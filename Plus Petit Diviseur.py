# Variables
n = int(input("Nombre que vous voulez tester: "))
d = n
r = 0

while 1 < d:
    if n % d == 0:
        r = d
        d = d - 1
    else:
        d = d - 1
print(r)
