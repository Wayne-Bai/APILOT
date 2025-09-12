import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset("tips")

# Create KDE patch
sns.kdeplot(data=tips['total_bill'], fill=True, alpha=.3, color="xkcd:turquoise")

# Add box plot statistics
sns.boxplot(data=tips['total_bill'], color="red", boxprops={'facecolor':'none'})

# Draw plot
plt.show()
