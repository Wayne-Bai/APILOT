# Import pandas library
import pandas as pd

# Create a sample DataFrame with a string column
data = {
   'strings': ['hello-world', 'foo-bar-baz', 'python-pandas-numpy']
}
df = pd.DataFrame(data)

# Split strings around given separator/delimiter
df[['first','second', 'third']] = df['strings'].str.split('-', expand=True, n=2)

# Print the resulting DataFrame
print(df)
