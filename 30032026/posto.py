combustivel = input("Informe o combustível: A - Álcool e G - Gasolina: ")
litros = int(input("Quantos litros você comprou? "))
valorFinal= None

if combustivel == "A":
    valor = litros * 4.89
    if litros < 20:
        valorFinal = litros * 0.97
    else:
        valorFinal = litros * 0.95
elif combustivel == "G":
    valor = litros * 6.89
    if litros < 20:
        valorFinal = litros * 0.96
    else:
        valorFinal = litros * 0.94
else: 
    print("Informação inválida'")