
import pandas as pd

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'], 
        'Age': [25, 30, 35], 
        'Gender': ['Female', 'Male', 'Non-binary']}
df = pd.DataFrame(data)

# convert dataframe to dictionary
dict_df = df.to_dict()
print(dict_df)
