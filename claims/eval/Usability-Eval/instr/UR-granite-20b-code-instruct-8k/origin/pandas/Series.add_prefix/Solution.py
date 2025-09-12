
import pandas as pd

# Create a sample dataframe
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
df = pd.DataFrame(data)

# Define the prefix string
prefix = 'myprefix_'

# Add the prefix to the dataframe column labels
df.columns = [prefix + col for col in df.columns]

# Display the updated dataframe
print(df)
