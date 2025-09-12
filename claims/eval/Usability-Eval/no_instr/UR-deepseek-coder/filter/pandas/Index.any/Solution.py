import pandas as pd

# Example DataFrame
data = {
    'A': [False, False, False],
    'B': [False, True, False],
    'C': [False, False, False]
}

df = pd.DataFrame(data)

# Check if any element is Truthy
any_truthy = df.any().any()

print(any_truthy)
