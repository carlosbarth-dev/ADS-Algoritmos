#Verificar se os lados de um triângulo formam um triângulo isósceles.

a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if a == b or a == c or b == c:
    print("Triângulo Isósceles")
else:
    print("Não é Isósceles")