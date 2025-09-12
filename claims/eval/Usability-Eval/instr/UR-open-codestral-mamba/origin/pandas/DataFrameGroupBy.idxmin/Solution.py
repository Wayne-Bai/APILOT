import pandas as pd

# Assuming df is your DataFrame and 'column_name' is the column you want to find the minimum index for
df = pd.DataFrame({'A': [1, 2, np.nan, 4],
                   'B': [5, np.nan, 7, 8],
                   'C': [9, 10, 11, 12]})

def get_index_of_first_min(df, column_name):
    # Exclude NA/null values
    df = df.dropna(subset=[column_name])

    # Find the index of the first minimum value in the specified column
    index = df[column_name].idxmin()

    return index

# Use the function on your DataFrame and column
index = get_index_of_first_min(df, 'A')
print(index)
