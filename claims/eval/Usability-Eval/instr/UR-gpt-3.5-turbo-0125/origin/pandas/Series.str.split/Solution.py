
import pandas as pd

# Sample data
data = {'strings': ['apple,banana,cherry', 'orange,grape,kiwi']}

# Create DataFrame
df = pd.DataFrame(data)

# Split strings around comma delimiter
df['strings'] = df['strings'].str.split(',')

print(df)
