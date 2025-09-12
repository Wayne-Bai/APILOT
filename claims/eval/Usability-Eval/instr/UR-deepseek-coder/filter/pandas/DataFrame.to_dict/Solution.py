import pandas as pd

# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Convert DataFrame to dictionary
df_dict = df.to_dict(orient='records')

print(df_dict)
