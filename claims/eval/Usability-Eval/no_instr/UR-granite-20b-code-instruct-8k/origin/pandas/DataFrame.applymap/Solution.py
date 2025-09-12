import pandas as pd

# Sample Data
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [23, 54, 34, 83],
        'Gender': ['M', 'F', 'M', 'F']}

df = pd.DataFrame(data)

# Apply a function to a Dataframe elementwise
# Let's say we want to convert all the ages to float

df['Age'] = df['Age'].astype(float)
