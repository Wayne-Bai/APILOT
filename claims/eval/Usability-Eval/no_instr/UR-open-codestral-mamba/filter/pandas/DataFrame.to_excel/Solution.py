import pandas as pd

# Create a simple dataframe
df = pd.DataFrame({
   'A': ['foo', 'bar', 'baz', 'bar', 'foo'],
   'B': ['one', 'one', 'two', 'three', 'three'],
   'C': ['small', 'large', 'large', 'small', 'large'],
   'D': [10, 20, 30, 20, 10],
   'E': [20, 40, 50, 50, 60]
})

# Save the dataframe as an excel file
df.to_excel('output.xlsx', index=False, sheet_name='Sheet1')
