# Import the pandas library
import pandas as pd

# Create the first DataFrame
data1 = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'Score': [90, 85, 88]
}
df1 = pd.DataFrame(data1)

# Create the second DataFrame
data2 = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 20],
    'Score': [90, 85, 90]
}
df2 = pd.DataFrame(data2)

# Compare the two DataFrames and show the differences
diff_df = df1.compare(df2)

print("Original DataFrames:")
print(df1)
print()
print("Original DataFrames:")
print(df2)
print()
print("Differences:")
print(diff_df)
