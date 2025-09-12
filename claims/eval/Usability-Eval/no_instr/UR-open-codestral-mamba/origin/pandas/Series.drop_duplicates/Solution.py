import pandas as pd

# Assuming df is the DataFrame and 'col' is the column with duplicate values
def remove_duplicates(df, col):
    return df[col].drop_duplicates()

# Test the function
df = pd.DataFrame({'col': [1, 1, 2, 3, 3, 4, 5, 5]})
print(remove_duplicates(df, 'col'))
