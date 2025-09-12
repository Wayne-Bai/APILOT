
import pandas as pd

def is_truthy(element):
    return bool(element)

df = pd.DataFrame({'a': [1, 2, 3, np.nan], 'b': [4, 5, 6, 7]})

# Return whether any element in column "a" is Truthy
result = df['a'].apply(is_truthy)

print(result)
