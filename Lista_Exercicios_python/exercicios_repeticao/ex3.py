# Exercício 3: Quantos alunos têm 30 anos (100 alunos)
# Este programa conta quantos alunos têm exatamente 30 anos entre 100 alunos.
# Utiliza um contador que incrementa apenas quando a condição (idade == 30) é verdadeira.
# Ilustra o uso de estruturas condicionais dentro de loops para filtrar dados.

contador = 0
for i in range(100):
    idade = int(input(f"Digite a idade do aluno {i+1}: "))
    if idade == 30:
        contador += 1  # Incrementa o contador apenas para idades iguais a 30
print("Quantidade de alunos com 30 anos:", contador)
