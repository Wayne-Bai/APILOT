import pandas as pd
import numpy as np

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 56, 78]
}

# Create DataFrame
df = pd.DataFrame(data)

# Use the style.background_gradient method for a bar effect
styled_df = df.style.bar(subset=['Values'], color='lightblue')

# Display styled DataFrame with inline Pandas styling
styled_df
