import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "Country": ["USA", "UK", "Australia", "Germany"]
}
df = pd.DataFrame(data)

# Set 'Name' and 'Country' as the index
df.set_index(['Name', 'Country'], inplace=True)

# Display the DataFrame
print("Default Display:")
print(df)

# Hide the entire index
pd.options.display.index=False

# Display the DataFrame with hidden index
print("\nDisplay with Entire Index Hidden:")
print(df)

# Hide specific elements from the index
df.index = [str(x) for x in df.index if not isinstance(x, str)]

# Display the DataFrame with specific index elements hidden
print("\nDisplay with Specific Index Elements Hidden:")
print(df)
