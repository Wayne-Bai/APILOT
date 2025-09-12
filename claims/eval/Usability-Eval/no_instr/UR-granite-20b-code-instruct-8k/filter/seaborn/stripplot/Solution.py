import seaborn as sns
import matplotlib.pyplot as plt
# Load the example tips dataset
tips = sns.load_dataset("tips")

# Draw a nested boxplot and swarm plot
sns.swarmplot(x="day", y="total_bill", data=tips, color=".2")
sns.boxplot(x="day", y="total_bill", data=tips, color=" redundant")
sns.despine(offset=10, trim=True)
plt.show()
