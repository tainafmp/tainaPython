i = 0
somaPar = 0 
somaImpar = 0
soma = 0

while i < 10:
    i+= 1
    soma += i
    if i % 2 == 0:
        somaPar += i
    elif i % 2 != 0:
        somaImpar += i
    else:
        print("Inválido");

print(f"A variável soma par está com o valor {somaPar}")
print(f"A variável soma ímpar está com o valor {somaImpar}")
