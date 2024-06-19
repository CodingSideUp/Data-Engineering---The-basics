import mysql.connector


host = 'http://100.104.100.57'
user = 'root'
password = '123'
database = 'test'

# Connect to MySQL database
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Example: Create a table
table_creation_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
'''
cursor.execute(table_creation_query)

# Commit changes and close the connection
conn.commit()
conn.close()
