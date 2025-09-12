import pandas as pd

# Assuming df is your DataFrame with MultiIndex
df = pd.DataFrame({
   ('A', 'B'): [1, 2, 3],
   ('A', 'C'): [4, 5, 6],
   ('B', 'B'): [7, 8, 9]
}, index=['a', 'b', 'c'])

# Create a DataFrame with the levels of the MultiIndex as columns
df_columns = df.columns.to_frame().T
