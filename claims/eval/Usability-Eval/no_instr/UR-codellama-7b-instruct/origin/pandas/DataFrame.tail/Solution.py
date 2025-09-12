import pandas as pd

df = pd.read_csv('data.csv')
last_n_rows = df.tail(n=5)
