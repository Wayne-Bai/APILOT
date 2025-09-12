import pandas as pd

# Sample DataFrame
data = {
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C']
}
df = pd.DataFrame(data)

# Suffix labels with string suffix
suffix = '_suffix'
df.columns = [col + suffix for col in df.columns]

print(df)
