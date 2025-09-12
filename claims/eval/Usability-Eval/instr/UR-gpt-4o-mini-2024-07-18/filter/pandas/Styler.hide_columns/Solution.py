import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Hiding specific column headers by using a specific view
# For example, to hide the 'Age' column header:
df_hidden = df.drop(columns=['Age'])

# Display the DataFrame without the 'Age' column
print(df_hidden)
