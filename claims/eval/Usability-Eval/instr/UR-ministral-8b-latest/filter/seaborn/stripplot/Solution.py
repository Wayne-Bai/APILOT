import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'x': ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'C', 'D', 'D'],
        'y': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'category': ['cat', 'dog', 'cat', 'cat', 'dog', 'dog', 'dog', 'mouse', 'cat', 'mouse']}

# Create a DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Set up the plot
plt.figure(figsize=(8, 6))
plot = sns.scatterplot(data=df, x='x', y='y', hue='category', style='category', size='category',
                       sizes=10, size_norm=True, dodge=True, alpha=0.7, palette='pastel', edgecolor='w')

# Add title and labels
plt.title('Categorical Scatterplot with Jitter')
plt.xlabel('Category X')
plt.ylabel('Values Y')

# Show plot
plt.show()
