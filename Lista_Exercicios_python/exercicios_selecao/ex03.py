#Verificar se os lados de um triângulo formam um triângulo retângulo.

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Triângulo Retângulo")
else:
    print("Não é Triângulo Retângulo")