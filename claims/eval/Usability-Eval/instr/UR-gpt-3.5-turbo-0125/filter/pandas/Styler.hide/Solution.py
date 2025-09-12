
import pandas as pd

# Sample dataframe
data = {'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e'],
        'C': [0.1, 0.2, 0.3, 0.4, 0.5]}

df = pd.DataFrame(data)

# Hide column headers
with pd.option_context('display.show_dimensions', False):
    print(df)

# Hide row index
with pd.option_context('display.show_dimensions', False):
    print(df.to_string(index=False))
