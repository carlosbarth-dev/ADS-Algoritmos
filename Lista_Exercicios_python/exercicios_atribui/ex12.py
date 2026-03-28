# EXERCÍCIO 12 - Área do cilindro

pi = 3.14

raio = float(input("Raio: "))
altura = float(input("Altura: "))

# calculando partes separadas (mais fácil entender)
area_base = pi * (raio ** 2)
area_lateral = 2 * pi * raio * altura

# fórmula final
area_total = (2 * area_base) + area_lateral

print("Área total:", area_total)

# OBS:
# separar em partes ajuda MUITO a entender