# Import the pandas library
import pandas as pd

# Define the SQL query or database table
# For locally stored SQL files
# query = pd.read_sql_query('SELECT * FROM table_name','sqlite:///path/to/your/file.db')

# For SQLite database
# query = pd.read_sql_query('SELECT * FROM table_name','sqlite:///your_file.db')

# For PostgreSQL database
# Replace 'your_host', 'your_username', 'your_password', 'your_database' with your actual PostgreSQL credentials
# query = pd.read_sql_query('SELECT * FROM table_name', 'postgresql://your_host:your_port/your_database',
#                       username='your_username', password='your_password')

# For MySQL database
# Replace 'your_host', 'your_username', 'your_password', 'your_database' with your actual MySQL credentials
# query = pd.read_sql_query('SELECT * FROM table_name','mysql://your_host:your_port/your_database',
#                        username='your_username', password='your_password')

# For Oracle database
# query = pd.read_sql_query('SELECT * FROM table_name', 'oracle://your_host:your_port/your_database',
#                        username='your_username', password='your_password')

# Read SQL query or database table into a DataFrame
def read_sql_table_into_dataframe(host, database, username, password, table_name):
    try:
        engine = pd.sql.create_engine(f'postgresql://{username}:{password}@{host}:5432/{database}')
        df = pd.read_sql_table(table_name, engine)
        return df
    except Exception as e:
        print(e)

# To use this function, replace the placeholders with your actual database credentials
# read_sql_table_into_dataframe('your_host', 'your_database', 'your_username', 'your_password', 'table_name')
