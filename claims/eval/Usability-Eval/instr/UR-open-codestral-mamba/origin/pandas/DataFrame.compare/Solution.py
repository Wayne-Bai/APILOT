import pandas as pd

# create two simple DataFrames
df1 = pd.DataFrame({
    'Name': ['John', 'Mary', 'Tom'],
    'Age': [28, 24, 33],
    'Gender': ['Male', 'Female', 'Male']
})

df2 = pd.DataFrame({
    'Name': ['John', 'Mary', 'Tom'],
    'Age': [28, 24, 35],
    'Gender': ['Male', 'Female', 'Male']
})

# compare the two DataFrames
diff = df1.compare(df2)

# print the differences
print(diff)
