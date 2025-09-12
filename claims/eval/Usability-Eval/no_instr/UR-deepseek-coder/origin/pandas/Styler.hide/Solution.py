import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Hide the entire index and column headers
with pd.option_context('display.show_dimensions', False, 'display.show_index_names', False, 'display.show_column_names', False):
    print(df)

# Hide specific rows and columns from display
# For example, hide the first row and the 'B' column
df_hidden = df.copy()
df_hidden.drop(index=df.index[0], columns=['B'], inplace=True)
print(df_hidden)
