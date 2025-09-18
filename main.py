import psycopg2

conexao = psycopg2.connect(
    host = "localhost",
    database = "BloomStore_bd",
    user="postgres",
    password = "2008",
    port = "5432"
)



cursor = conexao.cursor()

cursor.execute("""CREATE TABLE produto(
            id_produto SERIAL PRIMARY KEY NOT NULL,
            nome_produto VARCHAR (150) NOT NULL,
            categoria_escolhida VARCHAR(9) NOT NULL,
            subcategoria_escolhida VARCHAR (50) NOT NULL,
            cor_produto VARCHAR(100) NOT NULL,
            informacao_produto TEXT NOT NULL,
            preco_produto DECIMAL NOT NULL,
            stock_produto INTEGER NOT NULL
            );
""")

conexao.commit()

cursor.close()
conexao.close()


