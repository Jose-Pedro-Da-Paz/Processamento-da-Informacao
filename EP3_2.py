n = int(input(""))
soma = maior = 0
menor = 8000000000000000000000000
count = 0
while count < n :
    a= int(input(""))
    soma += a
    
    if a <= menor :
        menor = a
    if a >= maior :
        maior = a
    count +=1    
        
med = soma /n
print(soma)
print(f'{med:.2f}')
if menor != 0 :
      print(menor)
print(maior)
