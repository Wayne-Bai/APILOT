
import pandas as pd

# Load the two DataFrames to compare
df1 = pd.read_csv('df1.csv')
df2 = pd.read_csv('df2.csv')

# Compare the two DataFrames and show the differences
difference = df1.compare(df2)
print(difference)
