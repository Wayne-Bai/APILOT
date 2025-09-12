# Required libraries
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
import numpy as np

# Assuming 'data' is your DataFrame and 'column' is the column you want to plot
data = sns.load_dataset('tips')  # replace with your data
column = 'total_bill'  # replace with your column

# Create KDE plot
kde = sns.kdeplot(data[column], shade=True, cut=0)

# Get the x and y coordinates of the KDE plot
points = kde.get_paths()[0].vertices
x = points[:,0]
y = points[:,1]

# Calculate kernel estimator
kde_estimator = np.sum(np.exp(-(x[np.newaxis,:] - data[column].values[:, np.newaxis])**2 / 2), axis=-1) / 6

# Get the indices to sort the KDE estimator
sort_idx = np.argsort(x)

# Create the patch
verts = list(zip(x[sort_idx], y[sort_idx]))

# Add the patch
polygon = PolyCollection([verts], facecolors='gray', edgecolors='k', linewidths=2, alpha=.3)

# Add the patch to current axes and set the aspect of the plot
plt.gca().add_collection(polygon)
plt.gca().set_aspect("auto")

# Add the statistics to the plot
stats = data[column].describe()
plt.text(0.05, 0.9, 'count: {0:.0f}'.format(stats['count']), transform=plt.gca().transAxes)
plt.text(0.05, 0.85, 'mean: {0:.2f}'.format(stats['mean']), transform=plt.gca().transAxes)
plt.text(0.05, 0.8, 'std: {0:.2f}'.format(stats['std']), transform=plt.gca().transAxes)
plt.text(0.05, 0.75, 'min: {0:.2f}'.format(stats['min']), transform=plt.gca().transAxes)
plt.text(0.05, 0.7, '25%: {0:.2f}'.format(stats['25%']), transform=plt.gca().transAxes)
plt.text(0.05, 0.65, '50%: {0:.2f}'.format(stats['50%']), transform=plt.gca().transAxes)
plt.text(0.05, 0.6, '75%: {0:.2f}'.format(stats['75%']), transform=plt.gca().transAxes)
plt.text(0.05, 0.55, 'max: {0:.2f}'.format(stats['max']), transform=plt.gca().transAxes)

# Show the plot
plt.show()
