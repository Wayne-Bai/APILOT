# Import pandas library
import pandas as pd

# Create a MultiIndex DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9],
}
index = pd.MultiIndex.from_tuples([('X', 'x'), ('X', 'y'), ('Y', 'z')], names=['lvl1', 'lvl2'])
df = pd.DataFrame(data=data, index=index)

# Create a DataFrame with the levels of the MultiIndex as columns
df_result = pd.DataFrame({
    'lvl1': df.index.get_level_values('lvl1'),
    'lvl2': df.index.get_level_values('lvl2'),
    'A': df['A'],
    'B': df['B'],
    'C': df['C'],
})

print(df_result)
