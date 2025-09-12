import pandas as pd

# Sample DataFrame creation
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Hide column headers when printing to console
# Note: You cannot literally hide headers in a DataFrame, but you can display data without them.
# One way is to convert to string and exclude headers.

print(df.to_string(header=False, index=False))
