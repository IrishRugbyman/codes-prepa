#Variables
choix=input("Tapez F si votre temperature est en Fahrenheit, sinon tapez C: ")
T=0
C=0

#Calculs
if choix=="F":
    T=float(input("Entrez la temperature en Fahrenheit: "))
    C = (5/9)*(T-32)
    print("Cela correspond à: ",C," Celsius")
else:
    C=float(input("Entrez la temperature en Celsius: "))
    T=((9/5)*C)+32
    print("Cela correspond à: ",T," Fahrenheit")

    
