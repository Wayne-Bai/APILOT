
import pandas as pd

# create a sample dataframe
data = {'Name': ['John', 'Mary', 'David'],
        'Age': [27, 31, 24],
        'Gender': ['Male', 'Female', 'Male']}
df = pd.DataFrame(data)

# hide the entire index/column headers
df_without_headers = df.rename_axis(None)
print(df_without_headers)
