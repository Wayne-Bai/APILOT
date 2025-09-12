# Importing pandas library
import pandas as pd
import json

# Sample JSON string
json_string = '''
[
    {
        "name": "John",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Alice",
        "age": 25,
        "city": "Los Angeles"
    },
    {
        "name": "Bob",
        "age": 40,
        "city": "Chicago"
    }
]
'''

# Load JSON string into Python dictionary
data = json.loads(json_string)

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# Print the resulting DataFrame
print(df)
