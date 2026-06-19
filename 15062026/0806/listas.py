lista =        [10,11,12,20,21,30,9]
#index/ posição  0  1   2  3  4  5

print(lista) #imprime a lista toda
print(lista[2]) #imprime o item da posição 2 - 3° item na lista
print(len(lista)) #imprime o tamanho da lista
print(type(lista)) #imprime o tipo de dado armazenado na lista -> list

ultimaPosicao = len(lista) - 1

print(lista[1:]) #vai apresentar a lista a partir do item de posição 1 até o final do conteúdo;
print(lista[:2]) #vai apresentar a lista a partir do início parando no item da posição 2;
print(lista[::-1]) #apresenta a lista com a ordem invertida

#range(start, stop, step)
#[start:stop:step]

#Métodos na lista 

#1 - Adicionar item a lista usando append

listaDois = [3, 9, 9, 8]
lista.append(listaDois)

print("Quantidade de vezes que o número 9 aparece: ", lista.count(9))
print("3)", lista)

listaTres = []

for i in range(1,6):
    num = int(input(f"{i}°  valor: "))
    listaTres.append(num)
    #print(i, lista)

print(f"A lista final é {listaTres}")