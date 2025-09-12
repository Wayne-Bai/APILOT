import pandas as pd
json_string = "{'Name': 'John', 'Age': 30, 'City': 'New York'}"
df = pd.read_json(json_string)
print(df)
