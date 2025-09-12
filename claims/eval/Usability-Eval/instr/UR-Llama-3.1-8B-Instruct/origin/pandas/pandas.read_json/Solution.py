# Import the pandas library
import pandas as pd

# Define the JSON string
json_string = '''
{
    "name": "John",
    "age": 30,
    "city": ["New York", "Chicago"]
}
'''

# Load the JSON string into a pandas DataFrame
df = pd.read_json(json_string)

# Print the resulting DataFrame
print(df)
