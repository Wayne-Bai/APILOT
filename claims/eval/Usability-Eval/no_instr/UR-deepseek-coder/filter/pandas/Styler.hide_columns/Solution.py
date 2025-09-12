import pandas as pd

# Sample DataFrame
data = {
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C'],
    'Column3': [True, False, True]
}
df = pd.DataFrame(data)

# Hide the column headers
with pd.option_context('display.show_dimensions', False, 'display.max_columns', None):
    print(df.to_string(header=False))

# Hide specific keys in the columns
hidden_keys = ['Column2']
visible_columns = [col for col in df.columns if col not in hidden_keys]
print(df[visible_columns])
