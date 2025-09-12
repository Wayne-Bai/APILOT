import pandas as pd

# create a sample dataframe
data = {'Name': ['John', 'Jane', 'Smith', 'Doe'],
        'Age': [23, 45, 67, 89],
        'Gender': ['Male', 'Female', 'Male', 'Female']}
df = pd.DataFrame(data)

# define the mapping function
def map_values(value):
    if value == 'John':
        return 'Johnie'
    elif value == 'Jane':
        return 'Janey'
    else:
        return value

# apply the mapping function to the dataframe
df['Name'] = df['Name'].apply(map_values)

print(df)
