import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()  # Fetch all results
        print("Query executed successfully")
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return None


# Replace with your MySQL database credentials
host = "195.35.59.14"
user = "u666555369_hipermedia"
password = "H1permedia-"
database = "u666555369_hipermedia"

# Example usage
connection = create_connection(host, user, password, database)

# Example query
query = """
SELECT a.nombre, a.telefono 
FROM galeria g 
JOIN autores a ON g.id_autor = a.id_autor 
WHERE LOWER(g.descripcion) LIKE LOWER('%pintura%');
"""

results = execute_query(connection, query)
if results:
    for row in results:
        print(row)

# Close the cursor and connection
if connection:
    connection.close()
