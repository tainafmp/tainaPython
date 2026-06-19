n = int(input("Informe a quantidade de números que serão lidos: "))

while n > 0:
    i = int(input("Informe o número do qual deseja descobrir o fatorial: "))
    resultado = 1
    for f in range(1, i + 1):
        resultado *= f
    print(f"{i}! = {resultado}")
    n -= 1