'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O
resultado do atleta será determinado pela média dos cinco valores restantes. Você
deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O
programa deve ser encerrado quando não for informado o nome do atleta.'''

nome = (input("Nome do atleta: "))

while nome != "":
    saltos = []
    somaSaltos = 0

    for i in range(0,5):
        distSaltos = float(input(f"Informe a distância do {i+1}° salto: "))
        saltos.append(distSaltos)
        somaSaltos = somaSaltos + distSaltos

    print(f"Nome: {nome}")
    print(f"Lista saltos: {saltos}")
    print(f"Média dos saltos: {somaSaltos / len(saltos)}m")
    
    nome = (input("Nome do atleta: "))
