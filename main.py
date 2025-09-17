import psycopg2

conexao = psycopg2.connect(
    host = "localhost",
    database = "BloomStore_bd",
    user="postgres",
    password = "2008",
    port = "5432"
)


# Open a cursor to perform database operations
cursor = conexao.cursor()
# Execute a command: create datacamp_courses table
cursor.execute("""CREATE TABLE cliente(
            id_cliente SERIAL PRIMARY KEY NOT NULL,
            nome_cliente VARCHAR (200) NOT NULL,
            contacto_cliente VARCHAR(9) NOT NULL CHECK (length(contacto_cliente) = 9),
            email VARCHAR (200) NOT NULL,
            morada TEXT NOT NULL,
            genero VARCHAR(20) NOT NULL CHECK (genero IN ('Feminino', 'Masculino'))
            );
""")
# Make the changes to the database persistent
conexao.commit()
# Close cursor and communication with the database
cursor.close()
conexao.close()
