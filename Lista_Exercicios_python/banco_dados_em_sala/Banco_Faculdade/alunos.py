# alunos.py
# Arquivo com as operações da tabela alunos (CRUD)

from Banco import conectar_banco
from mysql.connector import Error


def criar_tabela(conexao):
    """
    Cria a tabela caso ela ainda não exista.

    Anotação minha:
    Isso é útil porque evita erro caso o banco esteja vazio.
    """

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            data_nascimento VARCHAR(10),
            cpf VARCHAR(14) UNIQUE
        )
    """)

    conexao.commit()


# --------------------------------------------------

def cadastrar_aluno():
    conn = conectar_banco()

    if conn and conn.is_connected():

        criar_tabela(conn)

        cursor = conn.cursor()

        print("\n--- CADASTRO DE ALUNO ---")

        nome = input("Nome: ").strip()
        data_nasc = input("Data de Nascimento (DD/MM/AAAA): ").strip()
        cpf = input("CPF: ").strip()

        sql = "INSERT INTO alunos (nome, data_nascimento, cpf) VALUES (%s,%s,%s)"
        valores = (nome, data_nasc, cpf)

        try:
            cursor.execute(sql, valores)
            conn.commit()

            print("Aluno cadastrado com sucesso!")

        except Error as e:
            print("Erro ao cadastrar:", e)

        finally:
            cursor.close()
            conn.close()


# --------------------------------------------------

def listar_alunos():
    """
    SELECT
    Mostra todos os alunos cadastrados
    """

    conn = conectar_banco()

    if conn and conn.is_connected():

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM alunos")

        alunos = cursor.fetchall()

        print("\n--- LISTA DE ALUNOS ---")

        for aluno in alunos:
            print(aluno)

        cursor.close()
        conn.close()


# --------------------------------------------------

def atualizar_aluno():
    """
    UPDATE
    Atualiza o nome de um aluno pelo CPF
    """

    conn = conectar_banco()

    if conn and conn.is_connected():

        cursor = conn.cursor()

        cpf = input("CPF do aluno que deseja atualizar: ")
        novo_nome = input("Novo nome: ")

        sql = "UPDATE alunos SET nome=%s WHERE cpf=%s"

        valores = (novo_nome, cpf)

        cursor.execute(sql, valores)

        conn.commit()

        print("Aluno atualizado!")

        cursor.close()
        conn.close()


# --------------------------------------------------

def deletar_aluno():
    """
    DELETE
    Remove um aluno da tabela
    """

    conn = conectar_banco()

    if conn and conn.is_connected():

        cursor = conn.cursor()

        cpf = input("CPF do aluno que deseja deletar: ")

        sql = "DELETE FROM alunos WHERE cpf=%s"

        cursor.execute(sql, (cpf,))

        conn.commit()

        print("Aluno removido!")

        cursor.close()
        conn.close()