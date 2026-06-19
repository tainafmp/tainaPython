lista = []
contInt = 0
#Solicite que o usuário preencha uma lista de 5 valores inteiro.
for i in range(1,4):
    num = int(input(f"{i}º valor: "))
    lista.append(num)

#Depois percorra a lista e verifique quantos valores >= 10 ele informou.
#1) O valor armazendo
'''
for v in lista:
    if v >= 10:
        print(v)
        contInt = contInt + 1
'''
#2) O valor armazendo, atraves posição/index
'''
for n in range(0, len(lista)):
        if lista[n] >= 10:
            print(lista[n])
            contInt = contInt + 1
'''

for i in range(0,3):
    num = int(input(f"{i+1}° valor: "))
    lista.append(num)

    if lista[i] >= 10:
        contInt += 1