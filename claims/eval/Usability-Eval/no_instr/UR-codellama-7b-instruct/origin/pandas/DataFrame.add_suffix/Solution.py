
import pandas as pd

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Gender': ['Female', 'Male', 'Non-binary']}
df = pd.DataFrame(data)

# suffix the labels with the string "Smith"
df['Name'] = df['Name'].str.concat('Smith')
print(df)
