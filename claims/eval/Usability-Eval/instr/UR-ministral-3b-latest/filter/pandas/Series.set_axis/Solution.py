import pandas as pd

#Creating a simple dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [22, 25, 27]}
df = pd.DataFrame(data)

#Assigning specific index to the dataframe
df.index = ['Student1', 'Student2', 'Student3']

print(df)
