import pandas as pd

# Sample data
data = {'A': [1, 2, 3, 4], 'B': [4, 3, 2, 1]}
df = pd.DataFrame(data)

# Applying the bar chart style in the cell backgrounds
styled_df = df.style.bar(color='lightblue')

# To display the styled DataFrame
print(styled_df.render())
