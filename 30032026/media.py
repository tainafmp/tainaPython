nome = input("Informe seu nome: ")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1+n2)/2

if media <= 10 and media >= 6: print(f"O aluno {nome} está aprovado.")
elif media >= 4 and media <= 6: print(f"O aluno {nome} está em recuperação.")
elif media >=  0 and media < 4: print(f"O aluno {nome} está reprovado.")
else: print("As notas informadas são inválidas.")
    
