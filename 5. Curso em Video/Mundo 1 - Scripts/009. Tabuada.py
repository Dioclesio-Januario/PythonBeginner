num = int(input("Digite um numero: "))
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0

for e in tabuada:
    print("{} x {:2} = {}"
          .format(num, e, num*e))       # {:2} implica dois digitos ocupados.
