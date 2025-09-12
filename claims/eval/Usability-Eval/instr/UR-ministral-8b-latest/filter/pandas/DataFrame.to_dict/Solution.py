import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)

# Convert DataFrame to Dictionary
df_dict = df.to_dict(orient='records')

print(df_dict)
