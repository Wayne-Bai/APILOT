import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David'],
        'Age': [25, 27, 25, 30, 27, 22]}
df = pd.DataFrame(data)

# Remove duplicate values
df_unique = df.drop_duplicates()

print(df_unique)
