import pandas as pd
import json

# Example JSON string
json_str = '''
{
    "name": ["John", "Jane", "Doe"],
    "age": [30, 25, 22],
    "city": ["New York", "Los Angeles", "Chicago"]
}
'''

# Convert JSON string to a Python dictionary
data = json.loads(json_str)

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

print(df)
