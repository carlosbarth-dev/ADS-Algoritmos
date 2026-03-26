# Exercício 7: Soma das notas >= 5.0 (repetição do exercício 4)
# Este programa é idêntico ao exercício 4, calculando a soma das notas maiores ou iguais a 5.0.
# Serve como reforço do conceito de filtragem condicional em loops.

soma = 0
quantidade = int(input("Quantos alunos? "))
for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    if nota >= 5.0:
        soma += nota
print("Soma das notas >= 5:", soma)
