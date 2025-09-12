import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to check
def check_truthiness(df, column_name):
    return df[column_name].apply(bool)

# Usage
df = pd.DataFrame({
    'A': [True, False, True],
    'B': [0, 0, 0],
    'C': [1, 2, 3]
})

print(check_truthiness(df, 'A'))
