import seaborn as sns
import matplotlib.pyplot as plt

# Generate some sample data
data = sns.load_dataset("tips")

# Create a bar plot of the point estimates and errors
sns.barplot(x="total_bill", y="tip", hue="sex", data=data)
plt.show()
