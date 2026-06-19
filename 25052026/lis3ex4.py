#Foi feita uma pesquisa entre os habitantes de uma região e coletados os
#dados de altura e sexo (0=masc, 1=fem) das pessoas. Faça um programa
#que leia 50 dados diferentes e informe:
#a. a maior e a menor altura encontradas;
#b. a média de altura das mulheres;
#c. a média de altura da população;
#d. o percentual de homens na população.

sexo = None
quantMulheres = 0
quantHomem = 0
maiorAltura = 0
menorAltura = 0
mediaAltMulher = 0
mediaAltHomem = 0
mediaAltPop = 0

for i in range(1, 50):
    sexo = int(input("0 - Homem e 1 - Mulher: "))
    if sexo == 0:
        quantHomem +=1