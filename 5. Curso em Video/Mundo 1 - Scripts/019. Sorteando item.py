import random

L = []
x = 1
while x < 5:
    nome = input("Digite um nome: ")
    L.append(nome)
    x += 1

sorteado = random.choice(L)

print("Soteado: {}".format(sorteado))
