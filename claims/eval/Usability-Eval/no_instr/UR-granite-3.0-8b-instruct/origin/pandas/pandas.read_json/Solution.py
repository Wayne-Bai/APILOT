import pandas as pd

# Assuming json_string is your JSON string
json_string = '{"name": ["John", "Anna", "Peter"], "age": [28, 24, 35]}'

# Convert JSON string to pandas DataFrame
df = pd.read_json(json_string)

# Print the DataFrame
print(df)
