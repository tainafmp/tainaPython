tabuada=int(input("Informe a tabuada que deseja saber: "))
inicio=int(input("Informe em qual valor o cálculo irá iniciar: "))
fim=int(input("Informe em qual valor o cálculo irá terminar: "))
i = 0

for i in range(inicio, fim):
    resultado = i * tabuada
    print(f"O valor de {i} x {tabuada} = {resultado}")