# Exercício 12: Fatorial de um número
# Este programa calcula o fatorial de um número inteiro não negativo.
# O fatorial n! é o produto de todos os inteiros positivos menores ou iguais a n.
# Utiliza um loop for para multiplicação acumulativa, começando de 1 até n.
# Nota: Para n=0, fatorial é 1 por definição, mas o código assume n >= 1.

n = int(input("Digite um número: "))
fatorial = 1
for i in range(1, n+1):
    fatorial *= i  # Multiplicação acumulativa: fatorial = fatorial * i
print("Fatorial:", fatorial)
