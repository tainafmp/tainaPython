altura = []
num = 0
maiorAltura = 0
menorAltura = 0
continua = 1
cont = 0 

while num != 0:
    num = float(input(f"Informe a altura da pessoa {cont}º, exemplo: 1.75 "))
    altura.append(num)
    cont = cont + 1

altura.pop()
altura.sort()
print(f"Menor altura {altura[0]}")
altura.reverse
print(f"Maior altura {altura[0]}")