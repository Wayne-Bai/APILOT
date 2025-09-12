import pandas as pd
import json

# Sample JSON String
json_str = '{"Name": ["John", "Jane", "Doe"], "Age": [28, 24, 30]}'

# Convert JSON String into pandas object
df = pd.read_json(json_str)

df
