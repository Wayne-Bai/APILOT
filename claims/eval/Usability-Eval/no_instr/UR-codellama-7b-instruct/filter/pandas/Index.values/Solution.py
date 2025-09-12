import pandas as pd

# create a sample dataframe
data = {'Name': ['John', 'Mary', 'David'],
        'Age': [25, 31, 42],
        'Gender': ['Male', 'Female', 'Unknown']}
df = pd.DataFrame(data)

# print the index values of the dataframe
print(df.index)
