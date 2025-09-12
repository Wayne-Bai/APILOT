import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset("tips")

# Draw a categorical scatterplot using jitter to reduce overplotting
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

# Show the plot
plt.show()
