import pandas as pd

# Assuming the JSON string is stored in a variable named 'json_string'
json_string = '{"column1": [1, 2, 3], "column2": ["a", "b", "c"], "column3": [2.1, 2.2, 2.3]}'

# Convert the JSON string to a pandas DataFrame
data_df = pd.read_json(json_string)

# Display the DataFrame
print(data_df)
