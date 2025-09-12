import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 'non-empty', True],
    'B': [5, 'text', True],
    'C': [3, 'another', True]
}

df = pd.DataFrame(data)

# Check if all elements are Truthy
are_all_truthy = df.astype(bool).all().all()

print("Are all elements truthy:", are_all_truthy)
