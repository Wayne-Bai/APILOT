
import pandas as pd

# create a sample DataFrame
data = {'Name': ['John', 'Mary', 'Jane'],
        'Age': [25, 30, 35],
        'Gender': ['Male', 'Female', 'Female']}
df = pd.DataFrame(data)

# create another sample DataFrame
data2 = {'Name': ['Jane', 'John', 'Tom'],
         'Age': [30, 45, 60],
         'Gender': ['Female', 'Male', 'Male']}
df2 = pd.DataFrame(data2)

# compare the two DataFrames and show the differences
print(df.compare(df2))
