import seaborn as sns
import matplotlib.pyplot as plt

# Load a dataset (e.g., tips dataset from seaborn)
tips = sns.load_dataset("tips")

# Create an enhanced box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x="day", y="total_bill", data=tips)

# Add title and labels
plt.title("Enhanced Box Plot for Larger Datasets")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")

# Show the plot
plt.show()
