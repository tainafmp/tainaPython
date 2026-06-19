h1 = int(input("Qual a idade do primeiro homem? "))
h2 = int(input("Qual a idade do segundo homem? "))
m1 = int(input("Qual a idade da primeira mulher? "))
m2 = int(input("Qual a idade da segunda mulher? "))

if h1 > h2:
    maiorHomem = h1;
    menorHomem = h2;
elif h2 > h1:
    maiorHomem = h2;
    menorHomem = h1;
else:
    print("As idades são iguais. ")

if m1 > m2:
    menorMulher = m2;
    maiorMulher = m1;
elif m2 > m1:
    menorMulher = m1;
    maiorMulher = m2;
else: 
    print("Entre com uma idade válida. ");
    
soma = maiorHomem + menorMulher
print(f"A soma das idades do homem mais velho e da mulher mais velha é: {soma}.");

produto = menorHomem * maiorMulher
print(f"O produto entre a idade do homem mais novo com a idade da mulher mais velha é: {produto}");