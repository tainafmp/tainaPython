n = int(input("Quantos números deseja adicionar? "))
i1 = 0
i2 = 0 
i3 = 0
i4 = 0 

while n > 0:
    num = int(input("Informe o primeiro número: "))
    if num < 0 or num > 100:
        print("Valor inválido, informe um número de 0 a 100: ")
        continue
    elif num >= 0 and num <= 25:
        i1 += 1
    elif num > 25 and num <= 50  :
        i2 += 1
    elif num > 50 and num <= 75:
        i3 += 1
    elif num > 75 and num <= 100:
        i4 += 1
    else:
        print("Valor inválido")
    
    n -= 1

print(f"A quantidade de números em um intervalo 1 - 25 é {i1}")
print(f"A quantidade de números em um intervalo 26 - 50 é {i2}")
print(f"A quantidade de números em um intervalo 51 - 75 é {i3}")
print(f"A quantidade de números em um intervalo 76 - 100 é {i4}")