import seaborn as sns
import matplotlib.pyplot as plt

# Create example data
data = sns.load_dataset("tips")

# Create a line plot with markers showing point estimates and confidence intervals
sns.lineplot(data=data, x="day", y="total_bill", marker='o', err_style="bars", ci=68)

plt.show()
