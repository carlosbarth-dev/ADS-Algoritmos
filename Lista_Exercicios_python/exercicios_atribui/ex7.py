# EXERCÍCIO 7 - Média ponderada

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
D = int(input("D: "))

# fórmula com pesos diferentes
media = (A * 3 + B * 4 + C * 2 + D * 5) / 14

print("Média:", media)

# OBS:
# soma dos pesos = 14 (por isso divide por 14)