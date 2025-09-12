# Import the pandas library
import pandas as pd

# Assuming we have a DataFrame named 'df'
# You can replace this with your actual DataFrame
df = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': [6, None, 8, 9, 10],
    'C': [11, 12, 13, 14, 15]
})

# Function to remove missing values
def remove_missing_values(df):
    # Drop rows with any missing value
    df_without_rows = df.dropna()
    
    # Drop columns with all missing values
    df_without_columns = df_without_rows.dropna(axis=1)
    
    return df_without_columns

# Remove missing values
df_without_missing_values = remove_missing_values(df)

# Print the updated DataFrame
print(df_without_missing_values)
