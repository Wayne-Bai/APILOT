import pandas as pd
import json

# Let's suppose we have a JSON string
json_string = '{"column1": {"0": "value1", "1": "value2", "2": "value3"}, "column2": {"0": 1, "1": 2, "2": 3}}'

# Converting JSON string to Python Dictionary
python_dict = json.loads(json_string)

# Converting Python Dictionary to Pandas DataFrame
df = pd.DataFrame(python_dict)
