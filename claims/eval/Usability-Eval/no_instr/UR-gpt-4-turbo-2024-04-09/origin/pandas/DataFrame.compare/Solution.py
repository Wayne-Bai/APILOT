import pandas as pd

# Creating two sample dataframes
data1 = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40],
         'Job': ['Engineer', 'Doctor', 'Artist', 'Writer']}
df1 = pd.DataFrame(data1)

data2 = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [26, 30, 34, 41],  # Age changed for Alice and Charlie, and David
         'Job': ['Engineer', 'Chef', 'Artist', 'Writer']}  # Job changed for Bob
df2 = pd.DataFrame(data2)

# Compare the two dataframes and show the differences
differences = df1.compare(df2)
print(differences)
