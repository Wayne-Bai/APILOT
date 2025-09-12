# Import the pandas library
import pandas as pd

# Create a simple DataFrame for demonstration
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Score': [85, 90, 78, 92]
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Define a suffix string
suffix_str = '_df'

# Rename columns by suffixing the suffix string
df_suffix = df.add_suffix(suffix_str)

# Print the DataFrame with suffixed column labels
print("\nDataFrame with suffixed column labels:")
print(df_suffix)
