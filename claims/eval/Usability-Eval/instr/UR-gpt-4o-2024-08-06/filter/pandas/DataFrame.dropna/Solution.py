import pandas as pd

# Sample DataFrame with missing values
data = {'A': [1, 2, None, 4],
        'B': [None, 2, 3, 4],
        'C': [1, None, 3, 4]}

df = pd.DataFrame(data)

# Remove rows with missing values
df_cleaned = df.dropna()

# Print the cleaned DataFrame
print(df_cleaned)
