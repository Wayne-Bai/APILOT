
import pandas as pd

# Sample JSON data
data = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON string into Python dict
data_dict = json.loads(data)

# Convert Python dict to pandas DataFrame
df = pd.DataFrame(data_dict)

print(df)
