import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
        'Age': [20, 21, 19, 20, 18]}
df = pd.DataFrame(data)

# Return the index of the first occurrence of the max value over the 'Name' column
max_index_name = (df.loc[df['Name'] == df['Name'].max()]).head(1).index[0]

# Return the index of the first occurrence of the max value over the 'Age' column
max_index_age = (df.loc[df['Age'] == df['Age'].max()]).head(1).index[0]

print(f"Index of first occurence of max 'Name': {max_index_name}")
print(f"Index of first occurence of max 'Age': {max_index_age}")
