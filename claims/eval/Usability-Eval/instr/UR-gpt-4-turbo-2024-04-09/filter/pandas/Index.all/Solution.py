import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [True, False, True],
    'C': ['non-empty', '', 'text']
})

# Check if all elements are Truthy in each column
result = df.all()

print(result)
