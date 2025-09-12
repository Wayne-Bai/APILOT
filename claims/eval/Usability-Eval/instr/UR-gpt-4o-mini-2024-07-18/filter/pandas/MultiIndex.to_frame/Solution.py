import pandas as pd

# Create a MultiIndex
index = pd.MultiIndex.from_tuples(
    [('A', 1), ('A', 2), ('B', 1), ('B', 2)],
    names=['Letters', 'Numbers']
)

# Create a DataFrame using a dictionary
data = {
    'Value1': [10, 20, 30, 40],
    'Value2': [50, 60, 70, 80]
}

# Construct the DataFrame with MultiIndex
df = pd.DataFrame(data, index=index)

# Reset the index to have the MultiIndex levels as columns
df_reset = df.reset_index()

# Display the DataFrame
print(df_reset)
