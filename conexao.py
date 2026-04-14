
import mysql.connector
# Conexão com o banco
conexao = mysql.connector.connect(
host='localhost',
user='root',
password='Guto0912@',
database='PI'
)
cursor = conexao.cursor()
# ---------- POST: Inserir um novo usuário ----------
def Dinserir_usuario(nome, email):
    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    valores = (nome, email)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Usuário inserido com ID:", cursor.lastrowid)
# ---------- GET: Buscar todos os usuários ----------
def listar_usuarios():
    cursor.execute("SELECT id, nome, email FROM usuarios")
    for (id, nome, email) in cursor.fetchall():
        print(f"ID: {id}, Nome: {nome}, Email: {email}")
# Exemplo de uso
    Dinserir_usuario("Joice", "joice@email.com")
listar_usuarios()
# Fechar conexãoD
cursor.close()
conexao.close()
