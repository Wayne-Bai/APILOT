
import pandas as pd

# create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# convert the DataFrame to a dictionary
df_dict = df.to_dict()
