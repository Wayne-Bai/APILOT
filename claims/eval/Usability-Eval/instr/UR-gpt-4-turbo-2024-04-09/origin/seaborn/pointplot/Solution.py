import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset("tips")

# Create a line plot with error bars and markers
sns.lineplot(data=data, x="size", y="total_bill", markers=True, err_style="bars", ci=68)

plt.show()
