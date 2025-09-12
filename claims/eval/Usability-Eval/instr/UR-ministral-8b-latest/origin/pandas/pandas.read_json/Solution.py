import pandas as pd

# Convert a JSON string to pandas object
json_string = '{"name": "John", "age": 30, "city": "New York"}'
pandas_object = pd.read_json(io.StringIO(json_string))
print(pandas_object)
