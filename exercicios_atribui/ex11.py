# EXERCÍCIO 11 - Volume do cone

pi = 3.14

raio = float(input("Raio: "))
altura = float(input("Altura: "))

# V = (π * r² * h) / 3
volume = (pi * (raio ** 2) * altura) / 3

print("Volume:", volume)

# OBS: igual cilindro, mas divide por 3