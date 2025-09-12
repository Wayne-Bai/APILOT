
import pandas as pd

# Example usage
strings = ['apple,banana,orange', 'grape,kiwi,melon', 'pear,watermelon,orange']
df = pd.DataFrame({'Fruits': strings})
split_strings = df['Fruits'].str.split(',', expand=True)
print(split_strings)
