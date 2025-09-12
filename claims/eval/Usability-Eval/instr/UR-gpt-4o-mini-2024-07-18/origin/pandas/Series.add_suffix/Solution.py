import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Suffixing column names with a string
suffix = '_suffix'
df.columns = [col + suffix for col in df.columns]

print(df)
