#Desenvolver um algoritmo que leia a altura de pessoas e armazene em uma lista,
#até que o 0 (zero) seja informado.
#Este programa deverá calcular e mostrar :
#a. A menor altura do grupo;
#b. A maior altura do grupo;

altura = []
alt = None

while alt != 0:
    alt = float(input(f"Informe a altura da pessoa: "))
    altura.append(alt)
    altura.sort()
print(f"A menor altura é {altura[0]}")
print(f"A maior altura é {altura[-1]}")

#não finalizado