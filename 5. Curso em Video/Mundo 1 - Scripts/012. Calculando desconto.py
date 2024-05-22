preco = float(input("Digite o valor do produto: "))

desconto = preco*(5/100)
novo_preco = preco - desconto

print("Preco inicial: {} mts".format(preco))
print("Desconto (5%): {} mts".format(desconto))
print("Novo preco: {} mts".format(novo_preco))
