import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

# Prefix labels with a string prefix
df.columns = ['_label_' + col for col in df.columns]

# Print the updated DataFrame
print(df)
