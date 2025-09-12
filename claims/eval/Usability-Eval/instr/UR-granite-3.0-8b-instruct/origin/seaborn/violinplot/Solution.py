import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.normal(size=100)

# Create a patch representing a KDE
kde = sns.kdeplot(data, shade=True)

# Add observations
plt.scatter(data, np.zeros_like(data), c='black', s=50)

# Add box plot statistics
box_data = [data[data < np.percentile(data, 25)],
            data[(np.percentile(data, 25)):(np.percentile(data, 75))],
            data[data > np.percentile(data, 75)]]
box_labels = ['25th percentile', 'Median', '75th percentile']
box_colors = ['blue', 'green', 'red']

for i, label in enumerate(box_labels):
    plt.boxplot(box_data[i], positions=[i+1], widths=0.5, patch_artist=True,
                boxprops=dict(facecolor=box_colors[i]),
                medianprops=dict(color='black'),
                whiskerprops=dict(color='black'),
                capprops=dict(color='black'),
                showmeans=True, meanline=True,
                meanprops=dict(color='black'))

plt.show()
