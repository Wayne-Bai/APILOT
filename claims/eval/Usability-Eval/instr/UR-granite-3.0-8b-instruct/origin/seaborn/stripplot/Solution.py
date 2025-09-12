import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame df with columns 'x' and 'y' for the categorical variables
# and 'z' for the numerical variable to be used for jittering

# Create a scatter plot with jittering
sns.scatterplot(x='x', y='y', hue='z', data=df, alpha=0.5)

# Add horizontal jittering
plt.gca().axes.set_xlim([-0.5, 1.5])
plt.gca().axes.set_xlim([-0.5, 1.5])

# Add vertical jittering
plt.gca().axes.set_ylim([-0.5, 1.5])
plt.gca().axes.set_ylim([-0.5, 1.5])

plt.show()
