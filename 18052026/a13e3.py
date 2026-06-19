i = 0
numNegativo = 0
while i <= 10:
    num = int(input("Entre com um número: "))
    if num < 0:
        numNegativo += num
    i += 1

print(numNegativo)

