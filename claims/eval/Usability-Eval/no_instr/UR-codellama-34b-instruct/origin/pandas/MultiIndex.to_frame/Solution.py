
import pandas as pd

# create a dictionary with the level values as keys and column names as values
level_dict = {'level_1': 'col1', 'level_2': 'col2'}

# create a DataFrame from the dictionary
df = pd.DataFrame(data=level_dict)

print(df)
