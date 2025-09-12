import pandas as pd
import numpy as np

# Create a simple dataframe
data = {'Col1': [1, 2, 3, 4], 'Col2': [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Use pandas styler to highlight maximum values
styled_df = df.style.highlight_max(color='lightgreen', axis=0)

# Save the dataframe as an HTML file
html = styled_df.render()

with open('output.html', 'w') as f:
    f.write(html)
