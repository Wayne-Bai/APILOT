# Importing pandas library
import pandas as pd

# Create a MultiIndex DataFrame
data = {
    'value': [1, 2, 3, 4, 5, 6]
}
df = pd.DataFrame(data, index=pd.MultiIndex.from_tuples(
    [
        ('a', 'x'), ('a', 'y'), ('b', 'x'), ('b', 'y'), ('c', 'x'), ('c', 'y')
    ],
    names=['letter', 'number']
))

print("Before sorting:")
print(df)

# Sort MultiIndex at the 'letter' level
df = df.sort_values(by='value')
df = df.sort_index(level=0)

# The result will respect the original ordering of the associated factor at that level.
print("\nAfter sorting at 'letter' level and then value column:")
print(df)

# Sort MultiIndex at the 'number' level
df = df.sort_index(level=1)

print("\nAfter sorting at 'number' level:")
print(df)
