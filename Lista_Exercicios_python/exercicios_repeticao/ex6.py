# Exercício 6: Média das notas
# Este programa calcula a média aritmética das notas de um grupo de alunos.
# Soma todas as notas e divide pelo número total de alunos.
# Introduz o conceito de média como medida estatística básica.

soma = 0
quantidade = int(input("Quantos alunos? "))
for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota
media = soma / quantidade
print("Média das notas:", media)
