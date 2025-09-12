import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create a categorical scatterplot with jitter
plt.figure(figsize=(10, 6))
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=tips, jitter=True)

# Show the plot
plt.show()
