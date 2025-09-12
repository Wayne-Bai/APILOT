
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset('tips')

# Creating the plot
sns.catplot(x="day", y="total_bill", kind="strip", data=tips, jitter=True)

plt.show()
