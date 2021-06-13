# uma função que:
#   recebe coordenadas como parâmetros para dois pontos cartesianos (plano sobre números Reais);
#   calcula e devolve a distância euclidiana entre os dois pontos dados.

# outra função que:
#   recebe coordenadas como parâmetros para um ponto cartesiano;
#   calcula e devolve a distância euclidiana entre a origem do plano e o ponto dado, chamando necessariamente a função 1 definida acima.

# um programa principal, em um bloco único, que:
#   lê as entradas necessárias para representar dois pontos cartesianos no plano dos Reais. 

#Obs: note que (0.3, -45.78) são coordenadas de um ponto válido;

# exibe a distância entre cada um dos pontos e a origem, chamando necessariamente sua função definida anteriormente;

# exibe a distância entre os dois pontos, chamando necessariamente sua função definida anteriormente.

def calculo_distancia(Ax, Ay, Bx, By):
  dAB = ((((Bx - Ax)**2) + ((By - Ay)**2))**(1/2))
  return dAB

def distancia_origem(x , y):
  dPO = calculo_distancia(x, y, 0, 0)
  return dPO

Ax = float(input("Ax:"))
Ay = float(input("Ay:"))
Bx = float(input("Bx:"))
By = float(input("By:"))

dAB = calculo_distancia(Ax, Ay, Bx, By)
dAO = distancia_origem(Ax , Ay)
dBO = distancia_origem(Bx , By)

print(dAB)
print(dAO)
print(dBO)