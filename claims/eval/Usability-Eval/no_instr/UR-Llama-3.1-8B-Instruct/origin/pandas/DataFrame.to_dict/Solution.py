import pandas as pd

# Creating a sample DataFrame
data = {
    "Name": ["Tom", "Nick", "John"],
    "Age": [20, 21, 19],
    "Score": [90, 85, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Converting the DataFrame to a dictionary
dictionary = df.to_dict(orient='records')

print("\nDictionary representation of the DataFrame:")
print(dictionary)
