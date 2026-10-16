import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "padaria"
)

print("Conectado!" if conexao.is_connected() else "Falhou")
conexao.close()