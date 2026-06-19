import random
numDado = [0, 0, 0, 0, 0, 0]
for i in range(0,100):
    dado = random.radint(1,6)

    if dado == 1:
        numDado[0] = numDado[0] + 1
    elif dado == 2:
        numDado[1] = numDado[1] + 1
    elif dado == 3:
        numDado[2] = numDado[2] + 1
    elif dado == 4:
        numDado[3] = numDado[3] + 1
    elif dado == 5:
        numDado[4] = numDado[4] + 1
    elif dado == 6:
        numDado[5] = numDado[5] + 1

print(f"N° 1 saiu: {numDado[0]}")
print(f"N° 2 saiu: {numDado[1]}")
print(f"N° 3 saiu: {numDado[2]}")
print(f"N° 4 saiu: {numDado[3]}")
print(f"N° 5 saiu: {numDado[4]}")
print(f"N° 6 saiu: {numDado[5]}")