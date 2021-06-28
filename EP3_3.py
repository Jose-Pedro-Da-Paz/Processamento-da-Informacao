Qestoque = int(input())
n = int(input())

Qsolicitadas = 0
cont = 0
i = 1
while i <= n:
    
    Qsolicitadas = int(input())
    
    if Qsolicitadas <= Qestoque:
        
        Qestoque = Qestoque - Qsolicitadas
        cont += 1
  
    i += 1
        
        
print(cont)
