import pandas as pd

# Create a sample data series
data = pd.Series(['apple,banana,orange', 'dog,cat', 'sun,moon,earth'])

# Split strings around the separator (comma in this example)
splitted_data = data.str.split(',')

print(splitted_data)
