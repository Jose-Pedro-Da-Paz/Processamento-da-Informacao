num = int(input(""))
alg1 = (num // 1000)
num = num - (alg1 * 1000)
alg2 = (num // 100)
num = num - (alg2 * 100)
alg3 = (num // 10)
num = num - (alg3 * 10)
alg4 = (num // 1)
num = num - (alg4 * 1)

alg1 -= 1
alg2 -= 1
alg3 -= 1
alg4 -= 1

alg1 = alg1 % 10
alg2 = alg2 % 10
alg3 = alg3 % 10
alg4 = alg4 % 10

print("{}{}{}{}".format(alg1,alg2,alg3,alg4))
