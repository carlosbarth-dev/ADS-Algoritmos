# Exercício 5: Soma de todas as notas
# Este programa calcula a soma total de todas as notas de um grupo de alunos.
# Utiliza um loop para coletar as notas e acumulá-las em uma variável.
# É um exemplo simples de agregação de dados numéricos.

soma = 0
quantidade = int(input("Quantos alunos? "))
for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma += nota
print("Soma das notas:", soma)
