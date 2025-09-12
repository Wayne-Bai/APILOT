import pandas as pd

# Assuming df is your DataFrame and it has object columns
df = pd.DataFrame({
    'A': ['1', '2', '3', '4'],
    'B': ['5', '6', '7', '8'],
    'C': ['a', 'b', 'c', 'd']
})

# Infer better dtypes for object columns
df = df.astype(object).apply(lambda x: x.astype('category' if x.dtype == 'object' else x.dtype))

# Print the DataFrame to see the inferred dtypes
print(df.dtypes)
