ladoA = float(input())
ladoB = float(input())
ladoC = float(input())

somaAB = ladoA + ladoB
somaAC = ladoA + ladoC
somaBC = ladoC + ladoB

if (ladoC < somaAB) and (ladoB < somaAC) and (ladoA < somaBC):
  print("VALIDO")
else:
  print("INVALIDO")
