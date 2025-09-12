import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

# Sample data
data = pd.DataFrame({
    'A': np.random.randint(1, 100, 10),
    'B': np.random.randint(1, 100, 10),
    'C': np.random.randint(1, 100, 10),
})

# Normalize data for plotting
norm = Normalize(vmin=data.min().min(), vmax=data.max().max())
cmap = ScalarMappable(norm=norm, cmap='Blues')

# Function to color cells
def background_gradient(s, cmap, width_factor=1):
    is_numeric = pd.to_numeric(s, errors='coerce').notna()
    return ['background-color: ' + cmap.to_rgba(val, bytes=True) 
            if is_numeric[i] else 'background-color: none' 
            for i, val in enumerate(width_factor * s.values)]

# Apply the function
styled_data = data.style.apply(background_gradient, cmap=cmap, width_factor=data.max().max())
styled_data
