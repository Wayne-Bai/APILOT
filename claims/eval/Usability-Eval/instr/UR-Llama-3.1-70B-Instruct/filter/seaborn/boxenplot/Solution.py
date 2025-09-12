# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate a random dataset
np.random.seed(0)
data = np.random.randn(100, 3)

# Create a DataFrame
df = pd.DataFrame(data, columns=['Category1', 'Category2', 'Category3'])

# Melt the DataFrame to prepare for seaborn
df_melted = pd.melt(df)

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Draw an enhanced box plot using seaborn
sns.boxplot(ax=ax, data=df_melted, x='variable', y='value', 
            showmeans=True, meanline=True, showfliers=False)

# Set labels and title
ax.set_title('Enhanced Box Plot')
ax.set_xlabel('Category')
ax.set_ylabel('Value')

# Show the plot
plt.tight_layout()
plt.show()
