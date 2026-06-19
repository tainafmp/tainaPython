inicio = int(input("Informe o número inicial: "))
fim = int(input("Informe o número final: "))
i = inicio
somaM3= 0
contM3 = 0

while i <= fim:
    i+=1
    if i % 3 == 0:
        somaM3 += i
        contM3 = contM3 +1
print(f"A soma dos múltiplos de 3 na faixa {inicio} e {fim} é: {somaM3}")
print(f"A quantidade de múltiplos de 3 é {contM3}")

