
import pandas as pd

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'], 
        'Age': [25, 30, 35], 
        'Gender': ['Female', 'Male', 'Non-binary']}
df = pd.DataFrame(data)

# hide the entire index from rendering
df.index = pd.Index(range(len(df)))
print(df)

# hide specific keys in the index from rendering
mask = df['Gender'] == 'Female'
df.index[mask] = np.nan
print(df)
