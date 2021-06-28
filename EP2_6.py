dia1 = int(input())
mes1 = int(input())
ano1 = int(input())

dia2 = int(input())
mes2 = int(input())
ano2 = int(input())

if ano1 > ano2:
  print("DATA2")
if ano2 > ano1:
  print("DATA1")

if ano1 == ano2:
  if mes1 > mes2:
    print("DATA2")
  if mes2 > mes1:
    print("DATA1")
  if mes1 == mes2:
    if dia1 > dia2:
      print("DATA2")
    if dia2 > dia1:
      print("DATA1")
    if dia1 == dia2:
      print("IGUAIS")
