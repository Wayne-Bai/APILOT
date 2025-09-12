import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'C'],
    'Values': [10, 20, 30]
}

df = pd.DataFrame(data)

# Use the pandas style API to apply background gradients
styled_df = df.style.bar(subset=['Values'], color='#FFA07A')

# The styled DataFrame can be rendered to HTML using the to_html method
# or displayed directly in a Jupyter notebook environment.

styled_df
