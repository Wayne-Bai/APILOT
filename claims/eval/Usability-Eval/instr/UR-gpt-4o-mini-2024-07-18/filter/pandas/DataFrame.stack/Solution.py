import pandas as pd

# Sample DataFrame creation
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# Stacking prescribed level(s) from columns to index
stacked_df = df.stack(level=None)  # You can specify a level if needed

print(stacked_df)
