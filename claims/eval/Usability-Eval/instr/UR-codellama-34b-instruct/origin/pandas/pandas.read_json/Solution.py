
import pandas as pd

# sample JSON data
data = '{"name": "John", "age": 30, "city": "New York"}'

# convert JSON string to pandas DataFrame
df = pd.json_normalize(data)

print(df)
