import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6],
    'c': [7, 8, 9]
})

# Define the suffix you want to add
suffix = '_suffix'

# Add suffix to the column names
df.columns = [col + suffix for col in df.columns]

# Display the DataFrame
print(df)
