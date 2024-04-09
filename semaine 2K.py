M = [[0, 1, 3, 0, 7], [0, 0, 1, 8, 0], [0, 0, 0, 4, 2], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
n = len(M)

for i in range(n):
    for j in range(n):
        if (i == 0 and j == 3) or (i == 1 and j == 4) or (i == 3 and j == 4):
            M[i][j] = -1

for i in range(5):
    print(M[i])

