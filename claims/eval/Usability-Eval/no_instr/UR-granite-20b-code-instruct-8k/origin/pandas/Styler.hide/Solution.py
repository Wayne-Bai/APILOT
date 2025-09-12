import pandas as pd

# Assuming you have a DataFrame called df
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Hide the index headers
df.style.hide_index()

# Hide the column headers
df.style.hide_columns()
