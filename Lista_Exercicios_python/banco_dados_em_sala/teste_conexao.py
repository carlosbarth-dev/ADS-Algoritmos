import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="cesb172004",   # coloque sua senha do MySQL aqui
        database="faculdade"
    )

    if conexao.is_connected():
        print("Conectado ao MySQL com sucesso!")

except Exception as erro:
    print("Erro ao conectar:", erro)