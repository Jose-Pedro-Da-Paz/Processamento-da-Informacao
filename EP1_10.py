VP = int(input())
FN = int(input())
FP = int(input())
VN = int(input())

acuracia = (VP + VN)/(VP + VN + FP + FN)
precisao =  (VP)/(VP + FP)
sensibilidade = (VP)/(VP + FN)

print("%.2f" %acuracia)
print("%.2f" %precisao)
print("%.2f" %sensibilidade)
