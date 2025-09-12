import pandas as pd

# Assuming df is your original DataFrame
df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz', 'qux'],
    'B': ['one', 'one', 'two', 'three'],
    'C': [1, 2, 3, 4],
    'D': [10, 20, 30, 40]
})

# Resetting the index
df_reset = df.reset_index(drop=True)

print(df_reset)
