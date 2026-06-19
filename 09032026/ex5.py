hn = int(input("Quantas horas normais você trabalha por dia? "))
he = int(input("Quantas horas extras você fez hoje? "))
sb = (hn * 10) + (he * 15)
sl = sb - (sb * 0.1)

print(f"Você trabalha {hn}H normalmente.")
print(f"Você fez {he}H extras.")
print(f"Seu salário bruto é R$ {sb} e o líquido R$ {sl}")