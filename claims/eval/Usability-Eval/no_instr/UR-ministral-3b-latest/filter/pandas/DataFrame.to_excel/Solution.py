import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John Doe', 'Jane Smith', 'Alice Johnson'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Write DataFrame to an Excel file
df.to_excel("example.xlsx", index=False)
