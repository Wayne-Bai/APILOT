# Import the pandas library
import pandas as pd

# Connect to the SQL database using your database credentials
# Replace 'your_database', 'your_username', 'your_password', and 'your_host' with your actual database credentials
# For example:
engine = pd.read_sql_database(
   'sqlite:///your_database.db',  # Path to the SQLite database file
    pool_pre_ping=True,
    connection_class=pd._libs.sql.DatabaseDialects['sqlite'].pooled_pysqlite_connection
)

# or

#SQL using conabase(eg) PostgreSQLserver
# Import Psycopg2 for postgresql and pyodbc driver for SQLserver 
import psycopg2
import pyodbc
# Replace your database credentials
# For example:
# PostgreSQL
params = {
    "host": 'your_host',
    "database": 'your_database',
    "user": 'your_username',
    "password": 'your_password',
}
conn = psycopg2.connect(**params)
query = "SQL Query Here"
df = pd.read_sql_query(query, conn)
conn.close()

# SQL server
server = 'your_host' 
database = 'your_database'
username = 'your_username'
password = 'your_password'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server +
                      ';DATABASE=' + database + ';UID=' + username +
                      ';PWD=' + password)
query = "SQL Query Here"
df = pd.read_sql_query(query, cnxn)
cnxn.close()

# With sqlite its like this:
# Assuming you are in the same directory as your database file.
db = 'your_database.db'  
query = "SQL Query Here"
df = pd.read_sql_query(query, db)

