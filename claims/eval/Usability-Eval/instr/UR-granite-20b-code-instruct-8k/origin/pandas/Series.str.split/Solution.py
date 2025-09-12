import pandas as pd

# Assuming the following dataframe 'df' with a column 'text' to split
# df = pd.DataFrame({'text': ['Hello,World!', 'How are you?']})

# Define the separator/delimiter to split the strings
separator = ','

# Split the strings in the 'text' column using the defined separator
df['split_text'] = df['text'].str.split(separator)

# Display the resulting dataframe
print(df)
