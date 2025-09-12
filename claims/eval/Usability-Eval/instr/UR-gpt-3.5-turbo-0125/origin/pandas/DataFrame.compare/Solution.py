
import pandas as pd

# Create two sample DataFrames
data1 = {'A': [1, 2, 3, 4],
         'B': ['apple', 'orange', 'banana', 'grape']}
df1 = pd.DataFrame(data1)

data2 = {'A': [1, 2, 5, 6],
         'B': ['apple', 'peach', 'banana', 'watermelon']}
df2 = pd.DataFrame(data2)

# Find the differences between the two DataFrames
diff_df = pd.concat([df1, df2]).drop_duplicates(keep=False)

print("Differences between the two DataFrames:")
print(diff_df)
