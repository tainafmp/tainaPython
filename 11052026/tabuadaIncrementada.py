tabuada = int(input("Informe a tabuada que deseja saber: "))
multiplicador = int(input("Informe em qual valor o cálculo vai iniciar: "))
multiplicando = int(input("Informe em qual valor o cálculo vai terminar: "))
produto = 0
i = multiplicador

while i < multiplicando:
    produto = tabuada * i
    print(f"{multiplicando} x {i} = {produto}")
    i +=  1