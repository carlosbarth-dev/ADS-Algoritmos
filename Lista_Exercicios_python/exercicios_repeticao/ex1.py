# Exercício 1: Soma das idades de 30 alunos
# Este programa calcula a soma das idades de 30 alunos, solicitando a entrada de cada idade via input.
# Utiliza um loop for para iterar 30 vezes, acumulando as idades em uma variável 'soma'.
# É uma aplicação básica de estruturas de repetição para processamento de dados sequenciais.

soma = 0
for i in range(30):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    soma += idade  # Acumula as idades em uma variável para somatório
print("Soma das idades:", soma)
