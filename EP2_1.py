nota1 = float(input())
nota2 = float(input())

MF = (nota1 + nota2)/2

if MF >= 5:
  print("%.2f"%MF)
  print("APROVADO")
else:
  print("%.2f"%MF)
  REC = float(input())
  MF = (MF + REC)/2
  if MF >= 5:
    print("%.2f"%MF)
    print("APROVADO") 
  else:
    print("%.2f"%MF)
    print("REPROVADO") 
