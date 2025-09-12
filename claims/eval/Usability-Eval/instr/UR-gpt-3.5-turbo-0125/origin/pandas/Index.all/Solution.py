
import pandas as pd

# Create a DataFrame
data = {'A': [True, False, True],
        'B': [True, True, True]}
df = pd.DataFrame(data)

# Check if all elements are truthy
all_truthy = df.all().all()
print(all_truthy)
