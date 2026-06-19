genero = input("Informe F para Feminino ou M para Masculino: ").upper()
altura = float(input("Informe sua altura: "))
pesoIdeal = None

if genero == "F" or genero == "f":  
    pesoIdeal = (62.1 * altura) - 44.7
elif genero.upper() == "M":
    pesoIdeal = (72.7 * altura) - 58
else:
    print("Informação inválida")