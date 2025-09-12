import pandas as pd

# Assume df is our DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
})

# Adding '_new' suffix to column labels
df.columns = [col + '_new' for col in df.columns]

df
