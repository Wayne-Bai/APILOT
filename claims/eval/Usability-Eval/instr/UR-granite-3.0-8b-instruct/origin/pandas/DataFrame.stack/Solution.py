import pandas as pd

# Assuming df is your DataFrame and 'column1', 'column2' are the columns you want to stack
df = pd.DataFrame({
    'column1': ['A', 'B', 'C'],
    'column2': ['D', 'E', 'F']
})

# Stack the columns
df_stacked = df.set_index('column1').stack()

print(df_stacked)
