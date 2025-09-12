import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]},
                  index=pd.MultiIndex.from_tuples([('one', 'A'), ('two', 'B'), ('three', 'A')], names=['first', 'second']))

df = df.sort_index()
