import pandas as pd

# Create a sample dataframe
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data=data)

# Hide the entire index
df.index.names = ['hidden_index']

# Hide specific keys in the index
df = df.reset_index()
df = df.rename(columns={'index': 'hidden_index'})

