# Sistema de Cadastro de Alunos com Python e MySQL

Projeto desenvolvido como atividade acadêmica para praticar integração entre **Python** e **banco de dados MySQL**.

O sistema permite cadastrar, visualizar, atualizar e excluir alunos armazenados em um banco de dados.

---

# Tecnologias Utilizadas

* Python 3
* MySQL
* mysql-connector-python
* Visual Studio Code
* MySQL Workbench

---

# Estrutura do Projeto

```
faculdade-python-mysql
│
├── main.py
├── banco.py
├── alunos.py
└── README.md
```

### Descrição dos arquivos

**main.py**

Arquivo principal do sistema.

Responsável por mostrar o menu no terminal e permitir que o usuário escolha operações como:

* Cadastrar aluno
* Listar alunos
* Atualizar aluno
* Deletar aluno
* Sair do sistema

---

**banco.py**

Arquivo responsável pela **conexão com o banco de dados MySQL**.

Centralizar a conexão em um arquivo separado evita repetição de código e facilita manutenção.

---

**alunos.py**

Arquivo responsável pelas **operações do banco de dados**, como:

* INSERT (cadastrar aluno)
* SELECT (listar alunos)
* UPDATE (atualizar aluno)
* DELETE (remover aluno)

---

# Banco de Dados

O sistema utiliza um banco de dados chamado:

```
faculdade
```

Tabela criada automaticamente pelo programa:

```
alunos
```

Estrutura da tabela:

| Campo           | Tipo         | Descrição                |
| --------------- | ------------ | ------------------------ |
| id              | INT          | Identificador automático |
| nome            | VARCHAR(100) | Nome do aluno            |
| data_nascimento | VARCHAR(10)  | Data de nascimento       |
| cpf             | VARCHAR(14)  | CPF do aluno             |

---

# Instalação

### 1 Instalar Python

Baixe em:

https://www.python.org

---

### 2 Instalar MySQL

Baixe:

* MySQL Server
* MySQL Workbench

---

### 3 Instalar biblioteca do MySQL no Python

No terminal execute:

```
pip install mysql-connector-python
```

ou caso o pip não funcione:

```
python -m pip install mysql-connector-python
```

---

# Criar Banco de Dados

No **MySQL Workbench** execute:

```
CREATE DATABASE faculdade;
```

---

# Executar o Projeto

No terminal do VS Code:

```
python main.py
```

O sistema exibirá um menu:

```
===== SISTEMA DE ALUNOS =====

1 - Cadastrar aluno
2 - Listar alunos
3 - Atualizar aluno
4 - Deletar aluno
5 - Sair

Escolha uma opção:
```

---

# Objetivo do Projeto

Este projeto foi desenvolvido para praticar:

* Conexão entre Python e banco de dados
* Comandos SQL (INSERT, SELECT, UPDATE, DELETE)
* Organização de código em múltiplos arquivos
* Estrutura básica de um CRUD
* Boas práticas iniciais de programação

---

# Observações

Projeto desenvolvido para fins acadêmicos no curso de **Análise e Desenvolvimento de Sistemas**.

O código contém comentários explicativos para facilitar o aprendizado e compreensão do funcionamento da integração entre Python e MySQL.

---

# Autor

Desenvolvido por **Carlos Barth**

Estudante de Análise e Desenvolvimento de Sistemas