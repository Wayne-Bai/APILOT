
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'Name': ['John', 'Doe', 'Jane'],
                   'Age': [25, 30, 35],
                   'Gender': ['Male', 'Female', 'Female']})

# Assign the desired index to the axis
df.index = df['Name']
