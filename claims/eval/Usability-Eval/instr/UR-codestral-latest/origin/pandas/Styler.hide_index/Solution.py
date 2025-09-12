import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data, index=['Idx1', 'Idx2', 'Idx3', 'Idx4'])

# Hide the entire index
df.style.hide_index()

# To hide specific keys in the index, let's say 'Idx2' and 'Idx4'
df.loc[df.index != 'Idx2'].loc[df.index != 'Idx4']
