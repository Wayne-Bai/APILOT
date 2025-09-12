
import pandas as pd

# Define the data frame and the column to split
df = pd.DataFrame({'text': ['this is a test', 'this is another test']})
col = 'text'

# Define the separator/delimiter
sep = ' '

# Split the strings around the separator/delimiter
split_df = df[col].str.split(sep).apply(pd.Series)

print(split_df)
