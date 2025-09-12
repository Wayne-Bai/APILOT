import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("tips")

# Create a bar plot with point estimates and error bars
sns.barplot(x="day", y="total_bill", data=data, ci="sd")

# Show the plot
plt.show()
