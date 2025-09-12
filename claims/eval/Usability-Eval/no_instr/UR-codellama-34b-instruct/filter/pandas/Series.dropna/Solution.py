
import pandas as pd

# create a sample dataframe with missing values
df = pd.DataFrame({'name': ['Alice', 'Bob', None, 'Dave'],
                   'age': [25, 30, None, 40]})

# remove missing values from the 'name' column
df['name'] = df['name'].dropna()

# remove missing values from the 'age' column
df['age'] = df['age'].dropna()

print(df)
