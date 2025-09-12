import pandas as pd

# Define the data
data = ['apple,banana,orange', 'grape,apple,kiwi', 'orange,pear,mango']

# Create a pandas DataFrame
df = pd.DataFrame(data, columns=['Fruits'])

# Split the strings around the comma delimiter
df['Split Fruits'] = df['Fruits'].apply(lambda x: x.split(','))

# Print the resulting DataFrame
print(df)
