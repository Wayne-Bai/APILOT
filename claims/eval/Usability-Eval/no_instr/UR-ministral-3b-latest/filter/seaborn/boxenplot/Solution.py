import seaborn as sns
import matplotlib.pyplot as plt

# Create a seaborn MSL (submerged) style object
plt.style.use('seaborn-mpl')

# Load the example dataset
tips = sns.load_dataset("tips")

# Create an enhanced box plot
sns.boxplot(x="day", y="total_bill", data=tips, orient="h", whis=[0, 100])

# Customize plot with fancy aesthetics
plt.title("Enhanced Box Plot of Total Bills per Day")
plt.xlabel("Total Bill")
plt.ylabel("Day")
plt.show()
