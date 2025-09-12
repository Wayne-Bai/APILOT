# Import pandas library
import pandas as pd

# Create a DataFrame
data = {
    'Group': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
}
df = pd.DataFrame(data)

# Compute product of group values
df['Product'] = df.groupby('Group')['Value'].transform(lambda x: x.cumprod())
df = df.drop_duplicates()

# Print the DataFrame
print(df)
