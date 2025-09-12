import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generating a larger sample dataset
np.random.seed(0)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C', 'D'], size=1000),
    'Value': np.random.randn(1000)
})

# Drawing an enhanced box plot for the larger dataset
plt.figure(figsize=(10, 6))
sns.violinplot(x='Category', y='Value', data=data, inner='box', linewidth=1)

# Customizing the plot
plt.title('Enhanced Box Plot with Violin Plot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.grid(True)

# Show the plot
plt.show()
