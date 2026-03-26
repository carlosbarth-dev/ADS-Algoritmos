#Verificar qual é o maior número e realizar a divisão do maior pelo menor.

n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

if n1 > n2:
    resultado = n1 / n2
else:
    resultado = n2 / n1

if resultado. is_integer():
    print("Resultado da divisão:", int(resultado))
else:
    print("Resultado da divisão:", resultado)