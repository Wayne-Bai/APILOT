import pandas as pd

# Create a sample dataframe
data = {
    'A': [1, 2, 3, 4],
    'B': ['x', 'y', 'z', 'w']
}

df = pd.DataFrame(data)

# Suffixing labels with a string
df.columns = [f'{col}_suffix' for col in df.columns]

print(df)
