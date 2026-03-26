# Exercício 4: Soma das notas >= 5.0
# Este programa calcula a soma das notas que são maiores ou iguais a 5.0, para um número variável de alunos.
# Primeiro, solicita a quantidade de alunos, depois itera coletando notas e somando apenas aquelas que atendem ao critério.
# Demonstra filtragem condicional em loops e processamento de dados com entrada dinâmica.

soma = 0
quantidade = int(input("Quantos alunos? "))
for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    if nota >= 5.0:
        soma += nota  # Soma apenas notas que atendem ao critério mínimo
print("Soma das notas >= 5:", soma)
