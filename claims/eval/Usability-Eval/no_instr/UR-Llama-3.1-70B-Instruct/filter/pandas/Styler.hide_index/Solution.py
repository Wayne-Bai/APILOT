# Import necessary library pandas
import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Germany']
}

df = pd.DataFrame(data)

# Display the DataFrame with index
print("DataFrame with Index:")
print(df)

# Hide the entire index from rendering
print("\nDataFrame without Index:")
print(df.to_string(index=False))

# Hide specific keys in the index from rendering
# Since DataFrame index in this example is integer based, 
# let's set 'Name' column as index and hide specific keys
df_set_index = df.set_index('Name')
# Now 'Name' column is the index
print("\nDataFrame after setting 'Name' as index:")
print(df_set_index)

# Let's hide John from rendering
# Since we cannot directly hide from index, we'll create a new DataFrame without 'John'
df_hide_john = df_set_index.drop('John')
print("\nDataFrame after hiding John:")
print(df_hide_john)
