import seaborn as sns
import matplotlib.pyplot as plt

# Example data
data = sns.load_dataset("tips")

# Plotting point estimates and errors using lines with markers
sns.pointplot(x="day", y="total_bill", data=data, markers='o', linestyles='-', ci="sd")

# Show the plot
plt.show()
