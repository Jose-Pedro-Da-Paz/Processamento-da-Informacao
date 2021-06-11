Ax = float(input("Ax:"))
Ay = float(input("Ay:"))
Bx = float(input("Bx:"))
By = float(input("By:"))

dAB = ((((Bx - Ax)**2)+((By - Ay)**2))**(1/2))

print("{:.2f}".format(dAB))