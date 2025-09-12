import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': ['cat', 'bat', 'ant', 'dog'],
    'B': [10, 20, 30, 40],
    'C': [1, 2, 1, 2]
})

# Prefix labels with string prefix
df = df.applymap(lambda x: 'prefix_' + str(x) if isinstance(x, (int, float)) else x)

# Display the transformed DataFrame
print(df)
