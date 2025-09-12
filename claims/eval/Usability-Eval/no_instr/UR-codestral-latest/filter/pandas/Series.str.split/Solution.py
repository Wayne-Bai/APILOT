# Import pandas
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
   'col': ['apple-banana-cherry', 'dog-cat-bird', 'red-green-blue']
})

# Define the separator/delimiter
sep = '-'

# Split the strings around the separator and create new columns for each part
df[['part1', 'part2', 'part3']] = df['col'].str.split(sep, expand=True)

# Print the DataFrame
print(df)
