import pandas as pd

# Sample data frame with missing values
data = {'Column1': [1, 2, None, 4],
        'Column2': ['A', 'B', 'C', None]}
df = pd.DataFrame(data)

# Remove rows with missing values
cleaned_df = df.dropna()

print(cleaned_df)
