import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Hide the entire index
df_hidden_index = df.reset_index(drop=True)

# Hide specific columns
df_hidden_columns = df.drop(['A', 'B'], axis=1)

# Hide specific rows
df_hidden_rows = df.drop([0, 2])
