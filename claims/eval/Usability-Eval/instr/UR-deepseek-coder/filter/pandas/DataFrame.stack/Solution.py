import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9],
    'D': [10, 11, 12]
}

df = pd.DataFrame(data)

# Stack the prescribed level(s) from columns to index
stacked_df = df.stack()

print(stacked_df)
