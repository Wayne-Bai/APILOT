import pandas as pd

# Create a DataFrame with duplicate values
data = {
    'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
    'Age': [20, 21, 19, 20, 19],
    'Score': [90, 85, 88, 90, 88]
}
df = pd.DataFrame(data)

# Drop duplicate values
unique_df = df.drop_duplicates()

# Print the unique Series
print(unique_df['Name'])
