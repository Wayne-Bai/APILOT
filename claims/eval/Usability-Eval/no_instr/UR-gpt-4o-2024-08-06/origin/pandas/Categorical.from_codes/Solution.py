import pandas as pd

# Create a DataFrame with codes and categories
data = {
    'codes': [1, 2, 3, 4],
    'categories': ['Low', 'Medium', 'High', 'Very High']
}

df = pd.DataFrame(data)

# Convert data to categorical type using the codes and categories
cat_type = pd.CategoricalDtype(categories=df['categories'], ordered=True)
df['codes'] = df['codes'].astype(cat_type)

print(df)
print(df.dtypes)
