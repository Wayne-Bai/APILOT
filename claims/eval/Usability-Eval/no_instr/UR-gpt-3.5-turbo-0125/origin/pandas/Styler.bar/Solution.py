
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dataframe
data = {
    'A': np.random.randint(1, 10, 10),
    'B': np.random.randint(1, 10, 10),
    'C': np.random.randint(1, 10, 10)
}
df = pd.DataFrame(data)

# Plotting bar chart in cell backgrounds
def highlight_max(s):
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]

df.style.apply(highlight_max)
