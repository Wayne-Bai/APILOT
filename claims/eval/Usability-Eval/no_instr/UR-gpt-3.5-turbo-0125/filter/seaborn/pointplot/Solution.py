
import matplotlib.pyplot as plt
import seaborn as sns

# Create some example data
import pandas as pd
data = pd.DataFrame({
    'x': range(10),
    'y': range(10),
    'yerr': range(1, 11)
})

# Use seaborn to plot point estimates and errors with lines and markers
sns.pointplot(x='x', y='y', data=data, yerr='yerr')
plt.show()
