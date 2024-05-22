largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura
tinta = area/2

print("Dimensao da parede: {}x{} m" .format(largura, altura))
print("Area: {} m^2" .format(area))
print("Tinta necessaria: {} Litros" .format(tinta))
