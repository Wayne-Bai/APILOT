# Import pandas library
import pandas as pd

# Create a simple dataframe
data = {'Name': ['John', 'Anna', 'Peter'],
        'Age': [28, 24, 22]}
df = pd.DataFrame(data)

# Assign a new index to the dataframe
new_index = ['index1', 'index2', 'index3']
df = df.set_index(pd.Index(new_index))

# Print the dataframe
print(df)
