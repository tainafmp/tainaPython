pao = 0.12
broa = 1.50
quantPao = int(input("Quantos pães foram vendidos? "))
quantBroa = int(input("Quantas broas foram vendidas? "))
arrecadado = (pao * quantPao) + (broa * quantBroa)
porc = 0.1 * arrecadado

print(f"Você deve guardar R${porc} em sua poupança.")