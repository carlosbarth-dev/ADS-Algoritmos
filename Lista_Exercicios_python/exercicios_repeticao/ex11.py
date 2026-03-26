# Exercício 11: Média das notas entre 5 e 7
# Este programa calcula a média das notas que estão estritamente entre 5.0 e 7.0.
# Similar ao exercício 10, mas para notas, ilustrando aplicação em diferentes contextos.

soma = 0
contador = 0
quantidade = int(input("Quantos alunos? "))
for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    if 5.0 < nota < 7.0:
        soma += nota
        contador += 1

if contador > 0:
    media = soma / contador
    print("Média das notas (5 < nota < 7):", media)
else:
    print("Nenhuma nota nesse intervalo")
