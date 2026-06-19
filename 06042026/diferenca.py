n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o segundo número: "))

if n1 > n2:
    maior = n1;
    menor = n2
elif n2 > n1:
    maior = n2;
    menor = n1;
else:
    print("Número inválido ou números são iguais. ")

dif = maior - menor;
print(f"A diferença entre o maior número {maior} e o menor {menor} é {dif}.")

