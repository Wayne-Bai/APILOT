# import pandas
import pandas as pd

# let's start with creating a simple DataFrame
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19]}
df = pd.DataFrame(data)

# now let's assume we want to assign a desired index
new_index = ['index1', 'index2', 'index3']

# we can use the DataFrame's set_index() method to do this
df = df.set_index(pd.Index(new_index))

# let's print the DataFrame to see the result
print(df)
