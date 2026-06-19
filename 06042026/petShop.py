atend = int(input("Quantos atendimentos tivemos nesta semana? "))

if atend <= 20:
    print("Ocioso");
elif atend > 20 or atend <= 30:
    print("Normal");
elif atend > 30:
    print("Alta demanda");
else:
    print("Informe um valor válido.")