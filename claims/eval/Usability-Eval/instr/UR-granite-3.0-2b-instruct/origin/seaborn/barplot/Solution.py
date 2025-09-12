import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create a sample dataset
np.random.seed(0)
data = np.random.normal(size=(100, 2))

# Create a DataFrame
df = pd.DataFrame(data, columns=['X', 'Y'])

# Calculate mean and standard deviation
mean_y = df['Y'].mean()
std_y = df['Y'].std()

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data as rectangular bars
sns.boxplot(x='X', y='Y', data=df, ax=ax, whis=1.5, showmeans=True, meanline=True, errorbar={'xerr': std_y, 'yerr': df['Y'] - mean_y})

# Set the title and labels
ax.set_title('Point Estimates and Errors as Rectangular Bars')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Show the plot
plt.show()
