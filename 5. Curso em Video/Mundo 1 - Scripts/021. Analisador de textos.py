nome = input("Nome completo: ")


print("Nome em maiusculas: {}".format(nome.upper()))
print("Nome em minusculas: {}".format(nome.lower()))
print("O nome tem {} caracteres".format((len(nome) - nome.count(" "))))
# print("Seu primeiro nome tem {} caracteres".format(nome.find(" ")))

separa = nome.split()
print("Primeiro nome: {}; E tem {} caracteres".format(
    separa[0], len(separa[0])))
