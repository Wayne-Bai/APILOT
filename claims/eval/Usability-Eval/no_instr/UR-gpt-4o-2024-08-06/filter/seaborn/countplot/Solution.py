import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'category': ['A', 'B', 'A', 'C', 'B', 'B', 'A', 'C', 'C', 'A']
}

# Create a bar plot to show the counts of observations in each categorical bin
sns.set_theme(style="whitegrid")
sns.countplot(x='category', data=data)

# Show the plot
plt.show()
