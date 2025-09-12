import pandas as pd

# Sample MultiIndex
index = pd.MultiIndex.from_tuples(
    [('A', 1), ('A', 2), ('B', 1), ('B', 2)], 
    names=['Letter', 'Number']
)

# Create an example DataFrame with the MultiIndex
data = pd.DataFrame({
    'Values': [10, 20, 30, 40]
}, index=index)

# Convert the levels of the MultiIndex into columns
df_with_columns = data.reset_index()

# Display the DataFrame
print(df_with_columns)
