from math import sqrt, hypot

co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))

# hp = sqrt((co**2) + (ca**2))
hp = hypot(co, ca)

print("Hipotenusa: {:.2f}".format(hp))
