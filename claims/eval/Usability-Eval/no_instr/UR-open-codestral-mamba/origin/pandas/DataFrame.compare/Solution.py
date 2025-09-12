import pandas as pd

# Consider the following two dataframes (df1 and df2)

df1 = pd.DataFrame({
   'A': ['A0', 'A1', 'A2', 'A3'],
   'B': ['B0', 'B1', 'B2', 'B3'],
   'C': ['C0', 'C1', 'C2', 'C3'],
   'D': ['D0', 'D1', 'D2', 'D3']},
   index=[0, 1, 2, 3])

df2 = pd.DataFrame({
   'A': ['A0', 'A1', 'A2', 'A3'],
   'B': ['B0', 'B1', 'B2', 'B3'],
   'C': ['C0', 'C1', 'C2', 'C3'],
   'D': ['D0', 'D1', 'D2', 'D4']},
   index=[0, 1, 2, 3])

# To compare and show the differences between these two dataframes
diff_df = pd.concat([df1, df2]).drop_duplicates(keep=False)
print(diff_df)
