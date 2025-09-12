import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 0, True, False, None, 'Hello'],
})

# Check if any element is truthy
is_truthy = df.astype(bool).any().any()
is_truthy
