import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# To hide only specific rows / columns from display
# use loc, iloc, or a condition. Here, let's hide row with index 1 and column 'A'.
df.loc[1, 'A'] = ''

# To hide the entire index / column headers
# use the style attribute with hide_index and hide_columns
display(df.style.hide_index().hide_columns('A'))
