faixa = 0
num = 1
while num != 0:
    num = int(input("Informe o número: "))
    if num >= 100 or num <= 200:
        faixa += 1

print(f"Foram informados {faixa} números na faixa indicada.")