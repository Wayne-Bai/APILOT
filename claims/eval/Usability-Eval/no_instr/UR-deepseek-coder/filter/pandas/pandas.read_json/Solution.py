import pandas as pd

# Sample JSON string
json_string = '''
[
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Anna", "age": 22, "city": "London"},
    {"name": "Mike", "age": 32, "city": "San Francisco"}
]
'''

# Convert JSON string to pandas DataFrame
df = pd.read_json(json_string)

# Display the DataFrame
print(df)
