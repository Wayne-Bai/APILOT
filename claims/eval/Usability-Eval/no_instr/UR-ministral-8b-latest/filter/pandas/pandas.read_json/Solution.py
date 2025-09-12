import pandas as pd

# Example JSON string
json_string = '''
[
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]
'''

# Convert JSON string to pandas DataFrame
data = pd.read_json(json_string, lines=True)

print(data)
