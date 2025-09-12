import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Create a categorical scatterplot with jitter
plt.figure(figsize=(10, 7))
sns.stripplot(data=tips, x="day", y="total_bill", jitter=True)

plt.title("Categorical Scatterplot with Jitter")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()
