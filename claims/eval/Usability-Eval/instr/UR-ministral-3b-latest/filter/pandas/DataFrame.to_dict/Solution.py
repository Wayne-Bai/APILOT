import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# Convert the DataFrame to a dictionary
df_dictionary = df.to_dict(orient='dict')

print(df_dictionary)
