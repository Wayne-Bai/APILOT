# Import seaborn library
import seaborn as sns
import matplotlib.pyplot as plt

# Load the sample dataset
tips = sns.load_dataset("tips")

# Create a KDE plot
sns.kdeplot(data=tips, x="total_bill", shade=True, fill=True, color="skyblue", alpha=0.5)

# Add box plot statistics
sns.boxplot(data=tips, x="total_bill", color="lightblue", showmeans=True, meanprops={"marker": "o", "markersize": 10}, zorder=10)

# Show the plot
plt.show()
