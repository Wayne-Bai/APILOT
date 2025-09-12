import pandas as pd

# Sample dataframe
data = {'text': ['apple,orange,banana', 'grapeberry,strawberry', 'kiwi,papaya', 'guava,passionfruit']}
df = pd.DataFrame(data)

# Split strings around the comma separator
df['splitted'] = df['text'].str.split(',', expand=True)

print(df)
