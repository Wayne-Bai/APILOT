import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 45],
    'City': ['New York', 'London', 'Paris']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to Excel
df.to_excel('output.xlsx', index=False)
