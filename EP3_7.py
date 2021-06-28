n = ()
m3 = 0
m5 = 0

while n != 0:
    n = int(input())
    
    if ((n%5) == 0) and ((n%3) == 0) and (n != 0):
        m3 += 1
        m5 += 1
        
    elif ((n%3) == 0) and (n != 0):
        m3 += 1
    
    elif ((n%5) == 0) and (n != 0):
        m5 += 1
       
print(m3)
print(m5)
