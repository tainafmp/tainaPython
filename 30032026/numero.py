num = int(input("Entre com um número: "))
imparPar = num % 2

if imparPar == 0: print(f"O número: {num} é par")
else: print(f"O número: {num} é ímpar")

if num < 0: print(f"O número: {num} é negativo")
elif num > 0: print(f"O número: {num} é positivo")
else: print("O número é neutro/zero")
