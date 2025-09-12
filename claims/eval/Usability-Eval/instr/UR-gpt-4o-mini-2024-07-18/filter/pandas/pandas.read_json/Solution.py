import pandas as pd
import json

# Sample JSON string
json_string = '{"name": ["Alice", "Bob"], "age": [25, 30], "city": ["New York", "Los Angeles"]}'

# Convert JSON string to Python dictionary
data_dict = json.loads(json_string)

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data_dict)

print(df)
