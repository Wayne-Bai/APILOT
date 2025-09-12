import pandas as pd

# Let's assume we have a Data Frame df
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [100, 200, 300, 400, 500],
    'C': ['one', 'two', 'three', 'four', 'five']
})

# And we have a function for example let's consider a lambda function that doubles values
def double(x):
    return x * 2

# Using applymap function to apply the function element wise
df = df.applymap(double)
print(df)
