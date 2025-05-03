import sqlite3

# Conecta ao banco de dados
conexao = sqlite3.connect('banco_de_dados.db')

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Cria a tabela usuarios se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    email VARCHAR
);
''')

# usuarios = [
#     { 'nome': 'Nicole', 'email': 'email@email.com'},
#     { 'nome': 'Thiago', 'email': 'email@email.com'},
#     { 'nome': 'Bruno', 'email': 'email@email.com'}
# ]

def cadastra_usuario(nome, email):
    # Inserir dados na tabela
    sql = "INSERT INTO usuarios (nome, email) VALUES (?, ?)"
    cursor.execute(sql, (nome, email))
    conexao.commit() 

cadastra_usuario('Nicole', 'oshirothiago@gmail.com')
 
def mostrar_usuarios()
    #  Usa uma query segura com parâmetros
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)

result = cursor.fetchall()

campo = 'nome'
valor = 'Nicole'

def selecionar_usuario()
# Usa uma query segura com parâmetros
sql = f"SELECT * FROM usuarios WHERE {campo} = ?"
cursor.execute(sql, (campo, valor,))

result = cursor.fetchall()

# Imprime os resultados
print(result)
for linha in result:
    print(linha)

# Atualiza dados na tabela
sql = "UPDATE usuarios SET nome = 'Joãozinho' WHERE id = 1"
cursor.execute(sql)
conexao.commit()

# Exclui dados da tabela
sql = "DELETE FROM usuarios WHERE id = 1"
cursor.execute(sql)
conexao.commit()

# Fecha a conexão com o banco de dados
conexao.close()

