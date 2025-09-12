import pandas as pd

# Sample data
data = {
    'id': [1, 2, 3],
    'value': [10, 20, 30]
}

# Create DataFrame
df = pd.DataFrame(data)

# Prefix labels with a string prefix
df.columns = 'prefix_' + df.columns

print(df)
