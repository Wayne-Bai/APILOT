import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Suffix each column label with a string
suffix = '_suffix'
df.columns = [f"{col}{suffix}" for col in df.columns]

print(df)
