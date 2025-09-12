import pandas as pd

# Sample DataFrame with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 30, 40],
    'City': ['New York', 'Los Angeles', None, 'Chicago']
}

df = pd.DataFrame(data)

# Remove rows with any missing values
df_cleaned = df.dropna()

print(df_cleaned)
