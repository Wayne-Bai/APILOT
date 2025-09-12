import pandas as pd

# Assume you have the following DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': ['one', 'two', 'three', 'four', 'five']
})

# Define a function that you want to use for mapping
def map_func(x):
    # This is a simple function that squares the input
    return x ** 2

# Apply the function to column 'A'
df['A_mapped'] = df['A'].apply(map_func)

# Now, df will have an additional column 'A_mapped' with the mapped values
print(df)
