import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("tips")

# Create a categorical scatterplot with points adjusted to be non-overlapping
sns.catplot(x="day", y="total_bill", data=data, kind="strip", jitter=True)

plt.show()
