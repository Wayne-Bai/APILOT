import pandas as pd

# Let's create a sample DataFrame
df = pd.DataFrame({
    'fruit': ['apple', 'banana', 'cherry', 'date']
})

# Let's create a mapping dictionary
mapping = {
    'apple': 'red',
    'banana': 'yellow',
    'cherry': 'red',
    'date': 'brown'
}

# Use the map function to apply the mapping to the 'fruit' column
df['color'] = df['fruit'].map(mapping)

print(df)
