# Import pandas library
import pandas as pd

# Create a DataFrame
data = {
    'codes': [1, 2, 3, 4, 5],
    'categories': ['A', 'B', 'A', 'B', 'C']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Convert 'codes' column to 'category' dtype and use that as the Categorical categories
# Convert 'categories' column to 'category' dtype as it is already of categorical type
cat = pd.Categoricalcategorias = df['categories'].astype('category')
df['codes_cat'] = df['codes'].astype('category').safe_encode(categories=cat.categories)

print("\nDataFrame with Categorical type:")
print(df.info())
print(df.head())
