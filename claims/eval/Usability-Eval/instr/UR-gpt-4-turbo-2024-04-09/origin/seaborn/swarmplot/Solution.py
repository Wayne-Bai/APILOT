import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a categorical scatterplot with non-overlapping points using dodge=True in stripplot
sns.stripplot(x="day", y="total_bill", data=tips, dodge=True)

# Show the plot
plt.show()
