import pandas as pd

# Sample DataFrame
data = {
    'Column1': [1, 2, 3],
    'Column2': ['A', 'B', 'C']
}
df = pd.DataFrame(data)

# Setting a new index
df.index = ['Row1', 'Row2', 'Row3']

print(df)
