import pandas as pd

# Example DataFrame
data = {'A': [True, False, True], 'B': [1, 2, 3], 'C': ['a', 'b', 'c']}
df = pd.DataFrame(data)

# Check if all elements in the DataFrame are Truthy
all_truthy = df.applymap(bool).all().all()

print(all_truthy)
