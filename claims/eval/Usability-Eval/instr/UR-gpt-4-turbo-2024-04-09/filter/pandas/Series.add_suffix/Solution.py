import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Apply string suffix to labels
df.columns = [f'{col}_suffix' for col in df.columns]
print(df)
