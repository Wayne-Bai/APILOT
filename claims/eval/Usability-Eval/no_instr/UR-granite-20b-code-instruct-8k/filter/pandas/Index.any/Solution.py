import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [True, False, True, False, True]
})

# Check if any element is Truthy
is_truthy = df['B'].any()

print(is_truthy)
