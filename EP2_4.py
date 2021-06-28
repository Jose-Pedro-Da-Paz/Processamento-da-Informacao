fab = int(input())
codigo = int(input())
distancia = float(input())

if (((fab >= 2001) and (fab <= 2020)) and (distancia > 5000)):
  print("SIM")
elif ((fab >= 1901) and (fab <= 2000)) and ((codigo == 100) or (codigo == 101)):
  print("SIM")
elif (fab == 2021) and ((codigo == 200) or (codigo == 201)) and (distancia > 200):
  print("SIM")
else:
  print("NAO")
