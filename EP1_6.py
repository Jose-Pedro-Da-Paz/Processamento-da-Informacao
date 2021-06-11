valor = float(input("Valor do produto: "))
desconto1 = (valor - (valor*(10/100)))
desconto2 = (desconto1 - (desconto1*(10/100)))
print("{:.2f}".format(desconto2))