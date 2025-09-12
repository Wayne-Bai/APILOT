import pandas as pd

# Sample data
data = {'text': ['apple,banana,grape', 'carrot,broccoli,spinach', 'orange,lime,lemon']}
df = pd.DataFrame(data)

# Split strings around given separator/delimiter
df['split_text'] = df['text'].str.split(',', expand=True)

# Print the DataFrame
print(df)
