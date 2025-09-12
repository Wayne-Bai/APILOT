import pandas as pd

# Example DataFrame with missing values
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4]
}
df = pd.DataFrame(data)

# Remove rows where any of the elements is missing
cleaned_df = df.dropna()
print(cleaned_df)
