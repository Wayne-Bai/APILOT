import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create a categorical scatterplot with jitter
sns.catplot(x="day", y="total_bill", kind="scatter", data=tips, jitter=True)

# Show the plot
plt.show()
