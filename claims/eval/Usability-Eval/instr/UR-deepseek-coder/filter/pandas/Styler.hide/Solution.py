import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Hide entire index and column headers
with pd.option_context('display.show_dimensions', False, 'display.show_index_names', False, 'display.show_column_names', False):
    print(df)

# Hide specific rows and columns
# Hide rows 1 and 2
hidden_rows = [1, 2]
# Hide columns 'B' and 'C'
hidden_columns = ['B', 'C']

# Display DataFrame with specific rows and columns hidden
print(df.drop(hidden_rows).drop(columns=hidden_columns))
