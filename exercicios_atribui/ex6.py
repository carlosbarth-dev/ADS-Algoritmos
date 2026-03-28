# EXERCÍCIO 6 - Hipotenusa

import math  # usado para raiz quadrada

lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))

# fórmula de Pitágoras
hipotenusa = math.sqrt((lado1 ** 2) + (lado2 ** 2))

print("Hipotenusa:", hipotenusa)

# OBS:
# ** = potência
# sqrt = raiz quadrada