import pandas as pd

# Suppose df is your DataFrame and 'column_name' is the column from which you want to remove duplicates
df = pd.DataFrame({
    'column_name': ['A', 'B', 'B', 'C', 'A', 'D', 'E', 'E']
})

unique_values = df['column_name'].drop_duplicates()

print(unique_values)
