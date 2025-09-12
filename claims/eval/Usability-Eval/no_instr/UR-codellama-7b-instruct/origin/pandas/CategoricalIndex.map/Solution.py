
import pandas as pd

# create sample dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': ['apple', 'banana', 'orange', 'grape', 'pineapple']})

# define mapping function
def map_values(value):
    if value == 1:
        return 'one'
    elif value == 2:
        return 'two'
    elif value == 3:
        return 'three'
    elif value == 4:
        return 'four'
    else:
        return 'five'

# map values in column A
df['A_mapped'] = df['A'].map(map_values)

print(df)
