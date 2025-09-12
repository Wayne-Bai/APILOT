import pandas as pd

# Sample DataFrame
data = {'Name': ['Tom', 'Nick', 'John', 'Peter'],
        'Age': [20, 21, 19, 18]}
df = pd.DataFrame(data)

# Hiding column headers (or index)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Print DataFrame without headers
print(df.to_string(index=False))
