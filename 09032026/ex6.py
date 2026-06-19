lata = int(input("Quantas latas foram compradas? "))
garrafa = int(input("Quantas garrafinhas foram compradas? "))
litro = int(input("Quantas garrafas foram compradas? "))
totalLitro = ((lata * 350 + garrafa * 600) / 1000) + litro * 2

print(f"Você comprou {totalLitro} litros de refrigerante.")