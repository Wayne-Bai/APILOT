import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'C'],
    'Value': [10, 20, 15, 25, 10, 30]
}
df = pd.DataFrame(data)

# Defining the mapping function or dictionary
mapping_dict = {'A': 'Apple', 'B': 'Banana', 'C': 'Cherry'}

# Using the `replace()` method to map values based on dictionary
df['Category_Mapped'] = df['Category'].replace(mapping_dict)

# Alternatively, using the `apply()` function with a lambda expression
df['Category_Mapped_Function'] = df['Category'].apply(lambda x: mapping_dict[x])

# Displaying the modified DataFrame
print(df)
