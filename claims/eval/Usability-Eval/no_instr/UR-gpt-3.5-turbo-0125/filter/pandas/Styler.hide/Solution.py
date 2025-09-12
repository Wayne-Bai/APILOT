
import pandas as pd

# Sample dataframe
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)

# Hide entire index and column headers
with pd.option_context('display.show_dimensions', False):
    print(df)

# Hide specific rows (index 1 and 3)
df_rows_hidden = df.drop([1, 3])
print(df_rows_hidden)

# Hide specific columns ('B' and 'C')
df_cols_hidden = df.drop(columns=['B', 'C'])
print(df_cols_hidden)
