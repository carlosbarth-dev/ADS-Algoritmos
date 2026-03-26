#Verificar se os lados de um triângulo formam um triângulo equilátero.

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a == b and b == c:
    print("Triângulo Equilátero")
else:
    print("Não é Equilátero")