# Import pandas
import pandas as pd

# Let's assume we have the following DataFrame
data = {
    'Label': ['A', 'B', 'C', 'D']
}

df = pd.DataFrame(data)

# Input string prefix
prefix = 'Prefix_'

# Prefix labels in the 'Label' column with the string prefix
df['Label'] = prefix + df['Label']

# Display the DataFrame
print(df)
