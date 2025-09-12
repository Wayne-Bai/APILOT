# Import necessary libraries
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Germany']
}
df = pd.DataFrame(data)

# Function to prefix column labels with a string
def prefix_column_labels(df, prefix):
    df.columns = [prefix + '_' + col for col in df.columns]
    return df

# Prefix column labels with 'person'
df_prefixed = prefix_column_labels(df, 'person')

# Print the resulting DataFrame
print(df_prefixed)
