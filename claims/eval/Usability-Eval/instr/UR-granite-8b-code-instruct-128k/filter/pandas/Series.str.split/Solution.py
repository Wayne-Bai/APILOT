import pandas as pd

# Create a sample dataframe with a string column
df = pd.DataFrame({'string_column': ['apple,banana,orange', 'grape,kiwi,pear', 'watermelon,strawberry,cherry']})

# Split the string column into multiple columns using the split function
df = df.assign(**df['string_column'].str.split(',', expand=True))

# Rename the columns to something more meaningful
df.columns = ['string_column'] + [' fruit_' + str(i+1) for i in range(len(df.columns)-1)]

# Print the resulting dataframe
print(df)
