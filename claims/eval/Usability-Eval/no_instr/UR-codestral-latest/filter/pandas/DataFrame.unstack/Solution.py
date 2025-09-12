import pandas as pd

# Assume df is your DataFrame and you want to pivot on columns 'A' and 'B'. The data will be aggregated using the 'mean' function.
df_pivot = df.pivot_table(index='C', columns=['A', 'B'], values='D', aggfunc='mean')
