import pandas as pd

# Sample DataFrame
data = {
    'A': ['apple', 'banana', 'cherry'],
    'B': ['dog', 'elephant', 'frog']
}

df = pd.DataFrame(data)

# Suffix labels with string suffix
df = df.add_suffix('_suffix')

print(df)
