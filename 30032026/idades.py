idade = int(input("Informe sua idade: "))

if idade >= 0 and idade <= 4:
    print("Não atendemos essa idade")
elif idade >= 5 and idade <= 7:
    print("Infantil A")
elif idade >= 8 and idade <= 10:
    print("Infantil B")
elif idade >= 11 and idade <= 13:
    print("Juvenil A")
elif idade >=14 and idade <= 17:
    print("Juvenil B")
elif idade >= 18:
    print("Você é adulto")
else: print("Entre com uma idade válida!")
    
print("FIM")