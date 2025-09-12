import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': ['x', 'y', 'z']
}
df = pd.DataFrame(data)

# Suffix labels with string suffix
df_with_suffix = df.rename(columns=lambda x: f'{x}_suffix')

print(df_with_suffix)
