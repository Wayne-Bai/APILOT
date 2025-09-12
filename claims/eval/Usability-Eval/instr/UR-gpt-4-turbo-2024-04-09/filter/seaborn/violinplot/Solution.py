import seaborn as sns
import matplotlib.pyplot as plt

# Load example data
data = sns.load_dataset("tips")

# Create a figure and a set of subplots
plt.figure(figsize=(8, 6))

# Draw a KDE plot with observations on top of it
sns.violinplot(x="day", y="total_bill", data=data, inner='stick', bw=0.2)

# Display the plot
plt.show()
