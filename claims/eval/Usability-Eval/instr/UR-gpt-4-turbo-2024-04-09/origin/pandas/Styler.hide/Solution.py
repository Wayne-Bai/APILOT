import pandas as pd

# Creating a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Example: Hiding index and column headers from display
with pd.option_context('display.show_index', False, 'display.show_column_names', False):
    print(df)

# Example: Hiding specific rows and columns (e.g., column 'A' and rows 0 and 2)
print(df.drop(index=[0, 2], columns=['A']))
