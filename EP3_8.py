n = int(input())
def primo(n) :
    if n < 2:
        return False
    for i in range (2,n):
        if n%i == 0 :
          return False
    return True
    
def nprimeiros(n) :
    primos = []
    x = 2
    while len(primos) < n :
        if primo(x) :
            primos.append(x)
        x = x + 1
    return primos

primos = nprimeiros(n)
print(primos)
