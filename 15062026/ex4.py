tamanho = int(input("Tamanho da lista: "))
lista = []

for i in range(0, tamanho):
    valor = int(input(f"{i+1}° valor: "))
    lista.append(valor)


for j in range(0, len(lista)):
    if lista[j] < 0:
        lista[j] = 0

