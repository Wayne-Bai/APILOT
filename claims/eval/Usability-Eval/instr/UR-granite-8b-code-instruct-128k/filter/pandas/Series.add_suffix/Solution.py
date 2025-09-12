
import pandas as pd

data = {'column': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)
df['column_suffix'] = df['column'].apply(lambda x: str(x) + '_suffix')
