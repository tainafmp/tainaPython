umCent = float(input("Quantas moedas de um centavo você tem? "))
cincoCent = float(input("Quantas moedas de cinco centavos você tem? "))
dezCent = float(input("Quantas moedas de dez centavos você tem? "))
vinteCincoCent = float(input("Quantas moedas de vinte e cinco centavos você tem? "))
cinquentaCent = float(input("Quantas moedas de cinquenta centavos você tem? "))
umReal = float(input("Quantas moedas de um real você tem? "))
total = (umCent * 0.01) + (cincoCent * 0.05) + (dezCent * 0.10) + (vinteCincoCent * 0.25) + (cinquentaCent * 0.5) + (umReal * 1)

print(f"Você economizou R$ {total}")