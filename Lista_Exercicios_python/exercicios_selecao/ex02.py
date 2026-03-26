#Verificar se um número está na faixa de 1 a 9.

numero = int(input("Digite um número inteiro: "))

if numero > 0 and numero < 10:
    print("Valor na faixa")
else:
    print("Valor fora da faixa")