
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataset
data = sns.load_dataset("tips")

# Adjust the jitter parameter to avoid overlapping points
sns.stripplot(x="day", y="total_bill", data=data, jitter=True, dodge=True)

plt.show()
