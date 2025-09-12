import pandas as pd

# Sample DataFrame creation
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# Hiding the column headers when displaying the DataFrame
print(df.to_string(header=False))
