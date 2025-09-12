import pandas as pd
import json

# Example JSON string
json_string = '''
[
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Anna", "age": 22, "city": "London"},
    {"name": "Mike", "age": 32, "city": "Chicago"}
]
'''

# Convert JSON string to a Python list of dictionaries
data = json.loads(json_string)

# Create a Pandas DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
