import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create DataFrame
df = pd.DataFrame(data)

# Hide column headers when printing the DataFrame
print(df.to_string(index=False, header=False))
