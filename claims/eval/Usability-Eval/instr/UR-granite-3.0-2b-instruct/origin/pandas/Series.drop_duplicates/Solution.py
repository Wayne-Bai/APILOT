import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column with duplicate values
df = pd.DataFrame({
    'column_name': [1, 2, 2, 3, 4, 4, 5]
})

# Remove duplicates
df_unique = df.drop_duplicates()

print(df_unique)
