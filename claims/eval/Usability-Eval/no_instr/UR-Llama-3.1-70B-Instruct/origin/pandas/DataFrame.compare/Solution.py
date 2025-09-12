# Import pandas library
import pandas as pd

# Function to compare two DataFrames and show the differences
def compare_dataframes(df1, df2):
    # Determine the differences in the DataFrames
    if not df1.equals(df2):
        df_diff = pd.merge(df1, df2, indicator=True, how='outer', suffixes=('_df1', '_df2'))
        # Select rows where the merge resulted in differences
        diff_df = df_diff[(df_diff['_merge']!= 'both') | (df_diff.eq(0).any(axis=1))]
        return df_diff, diff_df
    else:
        print("The DataFrames are identical")
        return None, None

# Create the DataFrames
df1 = pd.DataFrame({
   'key': ['K0', 'K1', 'K2', 'K3'],
   'A': ['A0', 'A1', 'A2', 'A3'],
   'B': ['B0', 'B1', 'B2', 'B3'],
   'C': ['C0', 'C1', 'C2', 'C3'],
   'D': ['D0', 'D1', 'D2', 'D3'],
})

df2 = pd.DataFrame({
   'key': ['K0', 'K1', 'K2', 'K3'],
   'A': ['A0', 'A1', 'A4', 'A5'],
   'B': ['B0', 'B1', 'B2', 'B3'],
   'C': ['C0', 'C1', 'C7', 'C8'],
   'D': ['D0', 'D1', 'D2', 'D3'],
})

# Compare the two DataFrames and show the differences
merged_diff, diff = compare_dataframes(df1.set_index('key'), df2.set_index('key'))

if diff is not None:
    print("Identified differences:")
    print(diff)
