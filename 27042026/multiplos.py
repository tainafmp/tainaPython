soma = 0 
valorInicial = int(input("Valor inicial: "))
valorFinal = int(input("Valor final: "))

for i in range(valorInicial, valorFinal): 
    if i % 3 == 0: 
        somaM3 += i

print(f"A soma dos múltiplos de 3 que existem entre {valorInicial} e {valorFinal} é: {somaM3}")