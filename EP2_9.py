codigo = int(input())

OO = codigo//10000 #código do planeta de origem
resto1 = codigo%10000

DD = resto1//100 #Código do planeta de destino
MM = resto1%100 #Código do modelo

if OO == 80:
    print("Marte")
if OO == 81:
    print("Saturno")
if OO == 90:
    print("Netuno")
if OO == 91:
    print("HD21749b")
    
if DD == 80:
    print("Marte")
if DD == 81:
    print("Saturno")
if DD == 90:
    print("Netuno")
if DD == 91:
    print("HD21749b")
    
if MM == 60:
    print("A6000")
if MM == 61:
    print("B7500")
if MM == 62:
    print("C9000")
