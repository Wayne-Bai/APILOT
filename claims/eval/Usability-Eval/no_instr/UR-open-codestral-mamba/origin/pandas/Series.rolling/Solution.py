import pandas as pd

# Let's assume we have a dataframe df
df = pd.DataFrame({
   'A': [1, 2, 3, 4, 5],
   'B': [10, 20, 30, 40, 50]
})

# To create a rolling window calculation, for instance a rolling mean, you can use the rolling() function.
# Here is a simple example of how you could create a rolling mean on column 'A':

df['A_roll'] = df['A'].rolling(window=2).mean()

print(df)
