import sqlite3

# Função para criar o banco de dados e as tabelas
def criar_banco_de_dados():
    # Conectar ao banco de dados (cria um novo arquivo se não existir)
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()

    # Criar a tabela Cardapio
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cardapio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL
        )
    ''')

    # Criar a tabela Contato
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Contato (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            mensagem TEXT NOT NULL
        )
    ''')

    # Salvar mudanças e fechar conexão
    conn.commit()
    conn.close()
    print("Banco de dados criado com sucesso!")

# Executar a função para criar o banco de dados
criar_banco_de_dados()
