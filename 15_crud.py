import sqlite3

def conectarBanco():
    local = r"C:\Users\integral\Desktop\PythonByanca\meuBanco.db"
    conexao = sqlite3.connect(local)
    return conexao

def criar_tabela():
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
       CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER
       )
    ''')
    conexao.commit()
    conexao.close()

def inserir_usuarios(nome, idade):
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
        VALUES (?,?)
    ''', (nome, idade))  
    conexao.commit()
    conexao.close()  

def ver_usuarios(): 
    conexao = conectarBanco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()   
    for usuario in usuarios:
        print(usuario)
    conexao.close()    

criar_tabela()
inserir_usuarios('byanca', '17')
ver_usuarios()    