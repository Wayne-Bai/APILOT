import pandas as pd

# create a DataFrame
df = pd.DataFrame({
    'A': [True, True, True],
    'B': [True, False, True],
    'C': [1, 2, 3]
})

# return whether all elements are Truthy
print(df.all().all())

# or you can also use
print(df.applymap(bool).all().all())

# or for specific column
print(df['A'].all())
