import sqlite3

# Conectando ao banco de dados (cria se não existir)
conn = sqlite3.connect('contatos.db')


# Criando um cursor para executar comandos SQL
cursor = conn.cursor()



# Criando a tabela 'contatos'

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone TEXT,
        email TEXT
    )
''')