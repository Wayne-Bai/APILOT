# Import the pandas library
import pandas as pd

# Create a DataFrame with an index
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
index = ['A', 'B', 'C', 'D']

df = pd.DataFrame(data, index=index)
print("Original DataFrame:")
print(df)

# Reset the index of the DataFrame
df_reset = df.reset_index()

# Create a new Series with the index reset
series_reset = pd.Series(df_reset['Age'], index=df_reset['Name'])

print("\nDataFrame with index reset:")
print(df_reset)

print("\nSeries with index reset:")
print(series_reset)
