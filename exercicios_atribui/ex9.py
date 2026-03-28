# EXERCÍCIO 9 - Prestação com atraso

prestacao = float(input("Valor da prestação: "))
taxa = float(input("Taxa de juros (%): "))
dias = int(input("Dias de atraso: "))

# fórmula do exercício
nova = prestacao + (prestacao * taxa * dias) / 100

print("Nova prestação:", nova)

# OBS:
# dividir por 100 porque a taxa é porcentagem