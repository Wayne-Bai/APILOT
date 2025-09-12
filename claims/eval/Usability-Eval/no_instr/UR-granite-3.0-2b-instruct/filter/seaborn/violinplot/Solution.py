import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Load the dataset (replace 'dataset.csv' with your actual dataset)
data = sns.load_dataset('dataset.csv')

# Calculate the KDE
kde = gaussian_kde(data['variable'])

# Create a patch representing the KDE
x = data['variable']
y = kde(x)

# Plot the KDE
plt.fill_between(x, y, alpha=0.2, color='blue')

# Add observations or box plot statistics
plt.boxplot(data['variable'], vert=False, showmeans=True, meanline=True)

# Show the plot
plt.show()
