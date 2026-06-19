num = int(input("Entre com número do qual deseja saber a tabuada: "))
i = 0

for i in range(1, 11):
    resultado = i * num
    print(f"O valor de {i} x {num} = {resultado}")