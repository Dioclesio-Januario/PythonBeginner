from time import sleep
from random import randint

print("-"*47)
print("Vou pensar num numero de 1 a 3, tente advinhar!")
print("-"*47)

n1 = randint(1, 3)
n2 = int(input("Em que numero eu pensei? "))

print("Processando...")
sleep(3)

if n1 == n2:
    print("Voce acertou")
else:
    print("Errou... Pensei no numero {}".format(n1))
