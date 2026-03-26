# Exercício 2: Média das idades de 50 alunos
# Este programa calcula a média aritmética das idades de 50 alunos.
# Primeiro, soma todas as idades usando um loop for, depois divide pela quantidade total.
# Demonstra o conceito de média como soma dividida pelo número de elementos.
# Em estatística, a média é uma medida de tendência central.

soma = 0
for i in range(50):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    soma += idade
media = soma / 50  # Cálculo da média: soma total dividida pelo número de alunos
print("Média das idades:", media)
