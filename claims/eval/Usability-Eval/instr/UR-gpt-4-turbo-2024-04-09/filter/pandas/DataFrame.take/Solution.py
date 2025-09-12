import pandas as pd

# Sample DataFrame
data = {'col1': [10, 20, 30, 40, 50],
        'col2': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

# Define positional indices
indices = [1, 3]

# Return elements at the given positional indices along a specified axis (default is 0)
selected_rows = df.iloc[indices]

print(selected_rows)
