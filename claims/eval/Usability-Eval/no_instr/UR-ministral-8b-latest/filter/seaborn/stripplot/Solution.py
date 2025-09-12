import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example data creation
data = pd.DataFrame({
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9]
})

# Create the strip plot
sns.stripplot(x='Category', y='Value', data=data, jitter=True)
# Show the plot
plt.show()
