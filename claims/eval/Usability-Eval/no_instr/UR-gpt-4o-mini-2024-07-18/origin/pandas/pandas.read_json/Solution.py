import pandas as pd
import json

# Example JSON string
json_string = '{"name": ["Alice", "Bob"], "age": [25, 30]}'

# Convert JSON string to Python dictionary
data = json.loads(json_string)

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
