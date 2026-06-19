salario = 1200
c1 = 200
c2 = 100
jurosUm = c1 + (c1 * 0.02)
jurosDois = c2 + (c2 * 0.02)
salarioFinal = salario - jurosDois - jurosUm
print(f"O que sobrou do seu salário foi: R$ {salarioFinal}")