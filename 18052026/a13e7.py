c = 1
maiorNumero = 0

while c != -1:
    c = int(input("Número positivo: "))

    if c > maiorNumero:
        maiorNumero = c
        
print(maiorNumero)