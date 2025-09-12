import pandas as pd

# Assume the JSON string is as follows
json_string = """
[
  {
    "Name": "John Doe",
    "Age": 30
  },
  {
    "Name": "Jane Doe",
    "Age": 25
  }
]
"""

# Convert JSON string to pandas DataFrame
df = pd.read_json(json_string)

print(df)
