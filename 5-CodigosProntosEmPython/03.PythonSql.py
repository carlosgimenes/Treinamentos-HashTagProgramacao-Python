import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=192.168.0.131,4483;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()


id = 3
cliente = "Gimenes Python"
produto = "Carro"
data = "25/08/2021"
preco = 5000
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()