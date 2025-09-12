
import pandas as pd

# Define the input DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z'], 'C': [4, 5, 6]})

# Create a MultiIndex from the columns of the DataFrame
index_names = df.columns
multi_index = pd.MultiIndex.from_tuples(zip(*[df[i].tolist() for i in index_names]), names=index_names)

# Pivot the DataFrame using the MultiIndex as new columns
pivoted_df = pd.DataFrame(df.values, index=multi_index[:-1], columns=multi_index[-1])

print(pivoted_df)
