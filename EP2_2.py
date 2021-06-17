salario = float(input())
vendas = float(input())

meta = salario * 0.50
comissao = vendas * 0.20

if comissao > meta:
  print("%.2f" %comissao)
  print("Atingiu meta de vendas")
else: 
  print("%.2f" %comissao)
  print("Nao atingiu meta de vendas")
