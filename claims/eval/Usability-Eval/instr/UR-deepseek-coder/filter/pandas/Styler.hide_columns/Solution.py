import pandas as pd

# Sample DataFrame
data = {
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C'],
    'Column3': [True, False, True]
}
df = pd.DataFrame(data)

# Hide specific column headers
hidden_columns = ['Column2']
visible_columns = [col for col in df.columns if col not in hidden_columns]

# Display the DataFrame with hidden column headers
print(df[visible_columns])
