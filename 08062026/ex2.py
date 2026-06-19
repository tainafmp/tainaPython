tam = int(input("Informe o tamanho da lista: "))
i = 0 
lista = []

for i in range(0,tam):
    num = int(input(f"{i+1}° valor: ")) #aqui ela mostra como não alterar a posição do item no array/lista mantendo o valor numa sequência "normal"
    lista.append(num)

print(lista[::-1])