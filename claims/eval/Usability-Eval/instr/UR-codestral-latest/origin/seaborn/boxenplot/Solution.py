import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame and 'variable' is the column name for which you want to draw the boxplot

# Set the style of seaborn
sns.set_style("whitegrid")

# Create the boxplot
plt.figure(figsize=(10, 7))
sns.boxplot(x=data['variable'], showfliers=False)

plt.title('Enhanced Boxplot of Larger Dataset')
plt.show()
