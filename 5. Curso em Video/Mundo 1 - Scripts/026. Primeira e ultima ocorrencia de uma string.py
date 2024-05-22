nome = input("Nome: ").lower()
nome = nome.strip()

print("A letra (A) aparece {} vezes".format(nome.count("a")))
print("A primeira letra (A) aparece na posicao {}".format(nome.find("a") + 1))
print("A ultima letra (A) aparece na posicao {}".format(
    nome.rfind("a") - nome.count(" ") + 1))
# print("A ultima letra (A) aparece na posicao {}".format(nome.rfind("a") + 1))
