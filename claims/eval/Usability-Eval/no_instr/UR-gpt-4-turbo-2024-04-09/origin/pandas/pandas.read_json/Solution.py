import pandas as pd
import json

# JSON string
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON string to pandas DataFrame
df = pd.read_json(json_data, typ='series')  # 'series' because the JSON represents a single record

print(df)
