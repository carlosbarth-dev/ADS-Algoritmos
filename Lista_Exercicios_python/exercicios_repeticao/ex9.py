# Exercício 9: Quantos alunos têm 30 anos (turma qualquer)
# Este programa conta quantos alunos têm exatamente 30 anos, para um número variável de alunos.
# Similar ao exercício 3, mas com quantidade dinâmica, reforçando contagem condicional.

contador = 0
quantidade = int(input("Quantos alunos? "))
for i in range(quantidade):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    if idade == 30:
        contador += 1
print("Quantidade de alunos com 30 anos:", contador)
