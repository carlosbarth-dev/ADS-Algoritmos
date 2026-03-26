# Exercício 8: Soma das idades > 25
# Este programa calcula a soma das idades dos alunos que têm mais de 25 anos.
# Filtra as idades maiores que 25 antes de somar, demonstrando seleção condicional.

soma = 0
quantidade = int(input("Quantos alunos? "))
for i in range(quantidade):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    if idade > 25:
        soma += idade  # Soma apenas idades acima do limite especificado
print("Soma das idades > 25:", soma)
