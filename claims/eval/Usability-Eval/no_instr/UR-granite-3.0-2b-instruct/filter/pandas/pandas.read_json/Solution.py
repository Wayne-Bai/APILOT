import pandas as pd

# Assuming json_string is your JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON string to pandas object
df = pd.read_json(json_string)

# Print the DataFrame
print(df)
