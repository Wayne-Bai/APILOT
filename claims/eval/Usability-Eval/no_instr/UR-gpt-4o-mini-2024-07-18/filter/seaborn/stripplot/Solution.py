import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Creating a strip plot with jitter
plt.figure(figsize=(10, 6))
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

# Show the plot
plt.title("Categorical Scatterplot with Jitter")
plt.show()
