
import pandas as pd

# read SQL query into a DataFrame
df = pd.read_sql('SELECT * FROM table_name', 'postgresql://username:password@host:port/database')
