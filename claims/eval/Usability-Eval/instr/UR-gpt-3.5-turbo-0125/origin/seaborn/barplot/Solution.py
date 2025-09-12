
import seaborn as sns
import matplotlib.pyplot as plt

# Create sample data
data = sns.load_dataset("tips")

# Create bar plot with point estimates as rectangular bars
sns.barplot(x="day", y="total_bill", data=data, ci="sd")

plt.show()
