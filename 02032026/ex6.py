dia = int(input("Que dia é hoje? "))
mes = int(input("Em que mês nós estamos? "))
quantDias = ((mes - 1) * 30) + dia

print(f"A quantidade de dias que se passaram desde o início do ano é: {quantDias}")