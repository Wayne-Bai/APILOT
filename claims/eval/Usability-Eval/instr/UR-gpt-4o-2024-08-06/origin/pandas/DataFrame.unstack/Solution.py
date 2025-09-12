import pandas as pd

# Sample data for demonstration
data = {
    'category': ['A', 'A', 'B', 'B'],
    'subcategory': ['a1', 'a2', 'b1', 'b2'],
    'value': [10, 20, 30, 40]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set the DataFrame index to be hierarchical
df.set_index(['category', 'subcategory'], inplace=True)

# Pivot the level of index labels to columns
# pivot_table is used for this kind of transformation in pandas
result = df.unstack()

# Print the resulting DataFrame
print(result)
