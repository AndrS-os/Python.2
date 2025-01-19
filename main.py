import sqlite3 


import sqlite3

# Conectando ao banco de dados (cria se não existir)
conn = sqlite3.connect('meu_banco.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

# Criando a tabela 'clientes'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT
    )
''')

# Inserindo dados na tabela
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ('João Silva', 'joao@email.com'))
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ('Maria Souza', 'maria@email.com'))

# Confirmando as alterações
conn.commit()

# Fechando a conexão
conn.close()