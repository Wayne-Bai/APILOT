# First import the pandas library
import pandas as pd

# Here is a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

# Define the suffix to be used
suffix = "_suffix"

# Rename columns using the suffix
df.columns = [str(col) + suffix for col in df.columns.values]
