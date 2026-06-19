nome = input("Informe o nome do produto: ");
quant = int(input("Informe a quantidade que você adquiriu deste produto: "));
preco = float(input("Informe o valor desse produto: "));

if quant <= 5:
    valor = (quant * preco);
    desconto = valor * 0.98;
    print(f"O valor total dos produtos comprados é de: {valor} e o valor com desconto {desconto} ");
elif quant > 5 and quant <= 10:
    valor = (quant * preco);
    desconto = valor * 0.97;
    print(f"O valor total dos produtos comprados é de: {valor} e o valor com desconto {desconto} ");
elif quant > 10:
    valor = (quant * preco);
    desconto = valor * 0.95;
    print(f"O valor total dos produtos comprados é de: {valor} e o valor com desconto {desconto} ");
else:
    print("Entre com valores válidos.")

