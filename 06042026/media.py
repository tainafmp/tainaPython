n1 = int(input("Entre com a sua primeira nota: "))
n2 = int(input("Entre com a sua segunda nota: "))
n3 = int(input("Entre com a sua terceira nota: "))
escolha = int(input("Para descobrir sua média escolha 1 - Aritmética e 2 - Ponderada: "))

if escolha == 1:
    media = (n1 + n2 + n3) / 3;
    print(f"Sua média aritmética é: {media}!")
elif escolha == 2:
    peso1 = 3;
    peso2 = 3;
    peso3 = 4;
    media = ((n1 * peso1) + (n2 * peso2) + (n2 * peso3))/ (peso1 + peso2 + peso3);
    print(f"Sua média ponderada é {media}!");
else: 
    print("Entre com valores válidos.")