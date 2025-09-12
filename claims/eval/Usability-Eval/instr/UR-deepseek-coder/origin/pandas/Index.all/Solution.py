import pandas as pd

# Example DataFrame
data = {'A': [True, True, False], 'B': [True, True, True]}
df = pd.DataFrame(data)

# Check if all elements are Truthy
all_truthy = df.all().all()

print(all_truthy)
