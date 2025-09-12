import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("tips")

# Enhanced box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x="day", y="total_bill", data=data, palette="Set3", showfliers=False)
sns.stripplot(x="day", y="total_bill", data=data, color="black", size=3, jitter=0.2)

# Adding title and labels
plt.title("Enhanced Box Plot of Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")

# Show plot
plt.show()
