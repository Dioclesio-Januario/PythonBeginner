import math

angulo = float(input("Angulo: "))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print("Seno: {:.3f} Cosseno: {:.3f} Tangente: {:.3f}".format(
    seno, cosseno, tangente))
