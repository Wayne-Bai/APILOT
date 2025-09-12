# Importing the pandas library
import pandas as pd

# Creating the first DataFrame
data1 = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'Score': [90, 85, 88]
}
df1 = pd.DataFrame(data1)

# Creating the second DataFrame
data2 = {
    'Name': ['Tom', 'Nick', 'Mary'],
    'Age': [20, 21, 22],
    'Score': [90, 85, 92]
}
df2 = pd.DataFrame(data2)

# Using the eq() function to compare the two DataFrames
df_diff = df1.ne(df2)

# Printing the differences
print("The differences are:")
print(df_diff)

# Using the isin() function to get values that are present in df2 but not in df1
diff1 = df2[df2['Name'].isin(df1['Name']) == False]

# Printing the values that are present in df2 but not in df1
print("\nValues present in df2 but not in df1:")
print(diff1)

# Using the isin() function to get values that are present in df1 but not in df2
diff2 = df1[~df1['Name'].isin(df2['Name'])]

# Printing the values that are present in df1 but not in df2
print("\nValues present in df1 but not in df2:")
print(diff2)
