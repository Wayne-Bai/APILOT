import pandas as pd

# Assuming df is your DataFrame
# Example DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
    'Score': [85, 90, 88, 92, 95]
}
df = pd.DataFrame(data)

# Compute min value of 'Score' for each 'Name'
grouped = df.groupby('Name')['Score'].min()

print(grouped)
