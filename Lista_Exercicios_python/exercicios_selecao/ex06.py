#Verificar se os lados de um triângulo formam um triângulo escaleno.

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a != b and a != c and b != c:
    print("Triângulo Escaleno")
else:
    print("Não é Escaleno")