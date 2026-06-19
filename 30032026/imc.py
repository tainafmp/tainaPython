altura = float(input("Informe a sua altura: "))
peso = float(input("Informe seu peso: "))
imc = peso / (altura ** 2)

if imc < 18.5: print("BAIXO PESO")
elif imc >= 18.5 and imc < 25: print("PESO IDEAL")
elif imc >= 25 and imc < 30: print("SOBREPESO")
elif imc > 30 : print("OBESIDADE")
else: print("Entre com um valor válido")
