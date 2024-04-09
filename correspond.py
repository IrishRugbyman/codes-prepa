LBZ = open("correspondanceLAMBOLEZ.txt", "w")
LBZ.write("Décimal Binaire Hexadécimal")
hexa = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
print("Décimal Binaire Hexadécimal")

for dec in range(0, 16):
    hex = hexa[dec]
    deci = dec
    (a, b, c, d) = (0, 0, 0, 0)
    while dec != 0:
        if dec % 2 == 1:
            d = 1
            dec = dec - 1
        else:
            if dec - 8 >= 0:
                a = 1
                dec = dec - 8
            else:
                a = 0
            if dec - 4 >= 0:
                b = 1
                dec = dec - 4
            else:
                b = 0
            if dec - 2 >= 0:
                c = 1
                dec = dec - 2
            else:
                c = 0

    LBZ.write("\n")
    LBZ.write(str(deci))
    LBZ.write("       ")
    LBZ.write(str(a))
    LBZ.write(str(b))
    LBZ.write(str(c))
    LBZ.write(str(d))
    LBZ.write("     ")
    LBZ.write(str(hex))
    print(deci, "     ", a, b, c, d, "    ", hex)

LBZ.close()
