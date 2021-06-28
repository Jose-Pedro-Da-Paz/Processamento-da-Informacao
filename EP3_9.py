import numpy as np

def contaDigito(n):
    return len( str(n) )

n = int(input())

alg = contaDigito(n)
x = np.zeros(alg+1)
j = 1

for i in range(alg, 0, -1):
    r = (n // (10**(i-1)))
    n = (n%(10**(i-1)))
    x[i] = r

for j in range(alg+1):
  if j != 0:
    saida = x[j]
    print("%.0f" %saida)
