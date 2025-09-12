import pandas as pd

json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = pd.read_json(json_string)

print(data)
