#Calcular as raízes de uma equação do segundo grau, utilizando a fórmula de Bhaskara. O programa deve solicitar os valores de A, B e C, e apresentar as raízes, ou uma mensagem informando que não existem raízes reais.

import math

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não Existe Valores Reais")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print("X1 =", x1)
    print("X2 =", x2)