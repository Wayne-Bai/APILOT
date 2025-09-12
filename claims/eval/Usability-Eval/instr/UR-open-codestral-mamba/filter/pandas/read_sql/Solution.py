import pandas as pd
from sqlalchemy import create_engine

def read_sql_query(query, database_url):
    engine = create_engine(database_url)
    df = pd.read_sql_query(query, engine)
    return df
