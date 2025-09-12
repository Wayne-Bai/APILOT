import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Create a simple plot
sns.set_theme(style="whitegrid")
ax = sns.scatterplot(x="total_bill", y="tip", data=tips)

# Configure the appearance of tick labels
ax.tick_params(axis='both', which='major', labelsize=10, labelcolor='red', rotation=45)
ax.tick_params(axis='both', which='minor', labelsize=8, labelcolor='blue', rotation=30)

# Show plot
plt.show()
