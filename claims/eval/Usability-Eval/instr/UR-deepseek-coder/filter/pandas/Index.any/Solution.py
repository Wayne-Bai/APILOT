import pandas as pd

# Example DataFrame
data = {'A': [0, 1, 2], 'B': [False, True, None]}
df = pd.DataFrame(data)

# Check if any element is Truthy
any_truthy = df.any().any()

print(any_truthy)
