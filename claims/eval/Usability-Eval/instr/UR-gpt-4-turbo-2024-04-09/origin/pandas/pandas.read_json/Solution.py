import pandas as pd
import json

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON string to Python dictionary
data = json.loads(json_string)

# Convert dictionary to pandas DataFrame
df = pd.DataFrame([data])

print(df)
