
import pandas as pd

# JSON string to convert to pandas object
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

# Convert JSON string to pandas object
df = pd.read_json(json_string, typ='series')

print(df)
