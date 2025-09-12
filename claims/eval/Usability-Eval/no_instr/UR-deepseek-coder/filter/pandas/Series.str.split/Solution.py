import pandas as pd

# Sample DataFrame
data = {'text': ['apple,banana,cherry', 'dog,cat', 'elephant,frog,giraffe,hippo']}
df = pd.DataFrame(data)

# Split strings around the delimiter ','
df['split_text'] = df['text'].str.split(',')

print(df)
