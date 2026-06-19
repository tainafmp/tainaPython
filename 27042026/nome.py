nome = input("Qual o seu nome completo? ")

for caracter in nome:
    if caracter == " ":
        break
    else:
        print(caracter)
        