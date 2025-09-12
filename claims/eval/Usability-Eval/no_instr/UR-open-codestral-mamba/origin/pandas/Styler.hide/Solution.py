import pandas as pd

# Assuming we have a DataFrame df
df = pd.DataFrame({
    'A': ['foo', 'bar', 'baz', 'qux'],
    'B': ['one', 'one', 'two', 'three'],
    'C': [1, 2, 3, 4],
    'D': [10, 20, 30, 40],
    'E': [100, 200, 300, 400]
})

# Hide the entire index / column headers
df.style.hide()

# Hide specific rows / columns from display
df.style.hide_index().hide_columns(['B', 'D'])
