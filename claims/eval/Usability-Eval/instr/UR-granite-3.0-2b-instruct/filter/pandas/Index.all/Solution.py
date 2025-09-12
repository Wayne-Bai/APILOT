import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [True, False, True],
    'B': [False, True, False],
    'C': [True, True, True]
})

# Check if all elements are Truthy
result = df.all()

print(result)
