#Solicite que o usuário preencha uma lista de 5 valores inteiro.
#Percorra a lista e verifique quantos valores são pares.

lista = []
contPar = 0


for i in range(0,5):
    num = int(input(f"{i+1}° valor: ")) #aqui ela mostra como não alterar a posição do item no array/lista mantendo o valor numa sequência "normal"
    lista.append(num)
    if num % 2 == 0:
        contPar += 1    
print(lista)
print(f"A quantidade de número pares é: {contPar}")