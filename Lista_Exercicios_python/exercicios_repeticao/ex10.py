# Exercício 10: Média das idades entre 25 e 40
# Este programa calcula a média das idades dos alunos que estão na faixa etária entre 25 e 40 anos (exclusivo).
# Utiliza um contador adicional para rastrear quantos alunos atendem ao critério, evitando divisão por zero.
# Demonstra média condicional e tratamento de casos especiais.

soma = 0
contador = 0
quantidade = int(input("Quantos alunos? "))
for i in range(quantidade):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    if 25 < idade < 40:
        soma += idade
        contador += 1  # Conta apenas alunos na faixa para cálculo preciso da média

if contador > 0:
    media = soma / contador
    print("Média das idades (25 < idade < 40):", media)
else:
    print("Nenhum aluno na faixa de idade")
