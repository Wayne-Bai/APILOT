import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset (I'm using the built-in tips dataset for this example)
tips = sns.load_dataset("tips")

# Draw a categorical scatterplot with jitter
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

# Show the plot
plt.show()
