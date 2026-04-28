import mysql.connector
conexao = mysql.connector.connect(
host='localhost',
user='root',
password='Leocurtulo.23',
database='PI'
)
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO eleitores
(cpf, nome_completo, titulo_eleitor, chave_acesso, is_mesario, status)
VALUES
('12345678900', 'Leonardo Curtulo', '99887766', 'abc123', True, 'Ativo')
""")

conexao.commit()

cursor.execute("SELECT * FROM eleitores")
print(cursor.fetchall())
