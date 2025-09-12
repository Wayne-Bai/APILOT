import pandas as pd

# create a sample dataframe
data = {'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35],
        'country': ['US', 'Canada', 'Mexico']}
df = pd.DataFrame(data)

# apply a function to the age column along the rows
def get_age_range(x):
    if x < 30:
        return 'young'
    else:
        return 'old'

# apply the function to the age column
df['age_group'] = df['age'].apply(get_age_range)
