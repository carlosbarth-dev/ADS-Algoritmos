# banco.py
# Arquivo responsável por fazer a conexão com o banco de dados

import mysql.connector
from mysql.connector import Error


def conectar_banco():
    """
    Essa função cria a conexão com o MySQL.

    Anotação minha:
    Estou deixando a conexão em um arquivo separado
    para não repetir esse código em todos os lugares.
    """

    try:
        # Primeiro, conectar sem especificar o banco para criar se necessário
        conexao_temp = mysql.connector.connect(
            host='localhost',
            user='root',
            password='cesb172004'  # colocar aqui a senha do MySQL se tiver
        )
        
        cursor_temp = conexao_temp.cursor()
        cursor_temp.execute("CREATE DATABASE IF NOT EXISTS faculdade")
        cursor_temp.close()
        conexao_temp.close()
        
        # Agora conectar ao banco
        conexao = mysql.connector.connect(
            host='localhost',
            database='faculdade',  # meu banco no MySQL Workbench
            user='root',
            password='cesb172004'  # colocar aqui a senha do MySQL se tiver
        )

        return conexao

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


if __name__ == "__main__":
    conexao = conectar_banco()
    if conexao:
        print("Conexão bem-sucedida!")
        conexao.close()
    else:
        print("Falha na conexão.")