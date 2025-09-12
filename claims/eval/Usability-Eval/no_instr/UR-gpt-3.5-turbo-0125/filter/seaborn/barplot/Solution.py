
import seaborn as sns
import matplotlib.pyplot as plt

# Create sample data
data = sns.load_dataset("tips")

# Plot with point estimates and error bars as rectangular bars
sns.barplot(x="day", y="total_bill", data=data, ci="sd", capsize=0.1)

# Display the plot
plt.show()
