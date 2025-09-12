# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset from seaborn
tips = sns.load_dataset("tips")

# Create a categorical scatterplot with points adjusted to be non-overlapping
plt.figure(figsize=(10, 6))
sns.stripplot(x="day", y="total_bill", jitter=False, data=tips)

# Show the plot
plt.title('Categorical Scatterplot')
plt.show()
