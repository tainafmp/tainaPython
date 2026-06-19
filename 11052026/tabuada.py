num = int(input("Entre com o número da tabuada que quer descobrir: "))
i = 0

while i < 10:
    resultado = num * i
    print(f"{i} x {num} = {resultado}")
    i+=1