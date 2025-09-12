
import pandas as pd

# Assuming we have a DataFrame df and we want to stack column 'B' and 'C' from level 0 to index

df = pd.DataFrame({
    'A': ['America', 'Europe', 'Asia'],
    'B': [1, 2, 3],
    'C': [4, 5, 6]
})

stacked_df = df.set_index(['A']).stack().reset_index()
stacked_df.columns = ['A', 'level', 'value']
print(stacked_df)
