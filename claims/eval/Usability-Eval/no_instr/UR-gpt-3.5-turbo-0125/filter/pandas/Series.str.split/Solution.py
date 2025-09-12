
import pandas as pd

# Create a sample dataframe
data = {'strings': ['apple,orange,banana', 'cat,dog', 'red,green,blue']}
df = pd.DataFrame(data)

# Split strings around comma
df['strings_split'] = df['strings'].apply(lambda x: x.split(','))

print(df)
