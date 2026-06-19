pares = 0

for n in range(0,500):
    somaPar = 0
    somaImpar = 0
    numPares = 0 
    numImpar  = 0
    if n % 2 == 0:
        print(n)
        somaPar+= n
        numPares+=1
    elif n % 2 == 1:
        print(n)
        somaImpar+= n
        numImpar+=1
    else:
        print("Entre com um valor válido. ")
    
    print(f"A soma dos números pares é {somaPar} e a quantidade de números pares é: {numPares}")
    print(f"A soma dos números ímpares é {somaImpar} e a quantidade de números ímpares é: {numImpar}")

