# Exercício 13: Verificar se um número é primo
# Este programa verifica se um número inteiro é primo.
# Um número primo é aquele maior que 1 que possui apenas dois divisores positivos: 1 e ele mesmo.
# O algoritmo conta os divisores verificando se n é divisível por cada i de 1 a n.
# Para eficiência, poderia otimizar verificando até sqrt(n), mas aqui mantemos a versão básica para clareza.

n = int(input("Digite um número: "))
contador = 0

for i in range(1, n+1):
    if n % i == 0:
        contador += 1  # Conta cada divisor encontrado

# Número primo tem exatamente 2 divisores
if contador == 2:
    print("É primo")
else:
    print("Não é primo")
