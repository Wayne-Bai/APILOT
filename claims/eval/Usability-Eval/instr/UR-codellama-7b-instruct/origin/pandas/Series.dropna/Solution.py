
import pandas as pd

# create sample data with missing values
data = {'Name': ['Alice', 'Bob', np.nan, 'Charlie'], 
        'Age': [25, 30, 35, 30], 
        'Gender': ['Female', 'Male', 'Unknown', 'Male']}
df = pd.DataFrame(data)

# use isnull() method to identify missing values and drop them
df.dropna(inplace=True)

# verify that missing values are gone
print(df)
