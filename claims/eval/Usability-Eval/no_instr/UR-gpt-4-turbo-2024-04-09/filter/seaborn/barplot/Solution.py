import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("tips")

# Create a bar plot to show point estimates and confidence intervals as error bars
sns.barplot(x="day", y="total_bill", data=data)

plt.show()
