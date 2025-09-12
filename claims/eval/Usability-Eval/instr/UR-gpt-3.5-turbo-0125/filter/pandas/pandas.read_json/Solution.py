
import pandas as pd

json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
data = pd.read_json(json_string, typ='series')
print(data)
