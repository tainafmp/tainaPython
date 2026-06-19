chico = 1.50
juca = 1.10
ano = 0

while juca < chico:
    chico += 0.02
    juca += 0.03
    ano +=1

print(f"Juca alcançou uma altura maior que a de Chico depois de {ano} anos, medindo {juca:.2f} cm. Com Chico medindo {chico:.2f} cm ")