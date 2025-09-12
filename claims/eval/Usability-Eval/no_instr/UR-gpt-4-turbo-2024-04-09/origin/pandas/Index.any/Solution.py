import pandas as pd

# Create a sample DataFrame
data = pd.DataFrame({
    'A': [0, 0, 0, 1],
    'B': [False, False, True, False],
    'C': [0, 0, 0, 0]
})

# Check if any element in the DataFrame is True (Truthy)
is_truthy = data.any().any()

print("Is there any truthy element in the DataFrame?", is_truthy)
