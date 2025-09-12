import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

# Convert the DataFrame to dictionary
df_dict = df.to_dict(orient='records')

# Print the dictionary
print(df_dict)
