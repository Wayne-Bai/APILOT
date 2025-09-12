
import pandas as pd

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Gender': ['Female', 'Male', 'Male']}
df = pd.DataFrame(data)

# group the dataframe by "Name" and compute max value of "Age"
max_age = df.groupby('Name')['Age'].max()

print(max_age)
