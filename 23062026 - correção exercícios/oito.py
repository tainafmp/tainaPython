anoNascimento = int(input("Em qual ano você nasceu? "))
ano = int(input("Em qual ano estamos? "))

idadeAnos = ano - anoNascimento
print(f"Sua idade em anos é: {idadeAnos}")

idadeMeses = idadeAnos * 12
print(f"Sua idade em meses é: {idadeMeses}")

idadeDias = idadeAnos * 365
print(f"Sua idade em dias é: {idadeDias}")

idadeSemanas = idadeAnos * 52
print(f"Sua idade em semanas é: {idadeSemanas}")
