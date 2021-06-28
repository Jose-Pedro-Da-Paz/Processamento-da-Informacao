carga = float(input())
Ax = float(input())
Ay = float(input())
Bx = float(input())
By = float(input())

distancia = ((((Bx - Ax)**2)+((By - Ay)**2))**(1/2))
print("%.2f" %distancia)


if carga <= 50000:
    if distancia <= 18000:
        print("SIM")
    elif distancia <= (18000*1.1):
        print("TALVEZ")
    else: 
        print("NAO")

elif carga <= 200000:
    if distancia <= 9000:
        print("SIM")
    elif distancia <= (9000*1.1):
        print("TALVEZ")
    else: 
        print("NAO")

elif carga <= 250000:
    if distancia <= 3000:
        print("SIM")
    elif distancia <= (3000*1.1):
        print("TALVEZ")
    else: 
        print("NAO")
else:
    print("NAO")
