saldo = float(input("Qual o seu saldo atual? "));

if saldo == 0 or saldo <= 200:
    print(f"Você não tem crédito");
elif saldo >= 201 or saldo <= 400:
    credito = saldo * (20/100);
    print(f"Seu saldo é de {saldo} e seu crédito é {credito}");
elif saldo >= 401 or saldo <= 600:
    credito = saldo * (30/100);
    print(f"Seu saldo é de {saldo} e seu crédito é {credito}");
elif saldo >= 601:
    credito = saldo * (40/100);
    print(f"Seu saldo é de {saldo} e seu crédito é {credito}");
else:
    print("Entre com um valor válido!");
    


