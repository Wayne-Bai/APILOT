import pandas as pd

# Sample DataFrame for demonstration
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Hide the entire index during display
with pd.option_context('display.show_dimensions', False):
    print(df.to_string(index=False))

# Hide specific columns (for example, 'B')
print(df[['A', 'C']].to_string(index=False))

# Hide specific rows (for example, first row)
print(df.iloc[1:].to_string(index=False))
