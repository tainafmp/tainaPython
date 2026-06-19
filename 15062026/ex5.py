'''Converta as temperaturas da lista celsius = [0, 15, 40] para fahrenheit e adicione a
lista fahrenheit = [].'''

celsius = [0, 15, 40]
fahrenheit = []
conversao = 0

for i in range (0, 3):
    conversao = 1.8 * celsius[i] + 32
    fahrenheit.append(conversao)

print(fahrenheit)