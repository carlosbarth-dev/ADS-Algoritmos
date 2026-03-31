# main.py
# Arquivo principal que roda o sistema

from alunos import (
    cadastrar_aluno,
    listar_alunos,
    atualizar_aluno,
    deletar_aluno
)


def menu():

    while True:

        print("\n===============================")
        print("     SISTEMA DA FACULDADE")
        print("===============================")

        print("1 - Cadastrar aluno")
        print("2 - Listar alunos (SELECT)")
        print("3 - Atualizar aluno (UPDATE)")
        print("4 - Deletar aluno (DELETE)")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            atualizar_aluno()

        elif opcao == "4":
            deletar_aluno()

        elif opcao == "5":
            print("\nEncerrando o sistema...")
            break

        else:
            print("Opção inválida!")


# isso garante que o menu rode quando executar o arquivo
if __name__ == "__main__":
    menu()