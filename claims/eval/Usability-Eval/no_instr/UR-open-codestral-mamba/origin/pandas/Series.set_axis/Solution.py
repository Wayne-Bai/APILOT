# Import pandas library
import pandas as pd

# Let's create a DataFrame for example
df = pd.DataFrame({'A': ['foo', 'bar', 'baz'],
                   'B': ['one', 'one', 'two'],
                   'C': [1, 2, 3],
                   'D': [10, 20, 30]})

# Set 'A' column as index
df = df.set_index('A')

# Check the DataFrame
print(df)
