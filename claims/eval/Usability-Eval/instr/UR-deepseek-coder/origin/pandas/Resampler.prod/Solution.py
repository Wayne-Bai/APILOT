import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'A', 'B', 'B', 'A'],
    'Value': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

# Compute the product of group values
grouped = df.groupby('Category')['Value'].apply(lambda x: x.cumprod().shift().fillna(1)).reset_index(drop=True)

# Add the result back to the original DataFrame
df['GroupProd'] = grouped

print(df)
