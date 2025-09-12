import seaborn as sns
import matplotlib.pyplot as plt

# Example dataset
tips = sns.load_dataset("tips")

# Create the strip plot with jitter
plt.figure(figsize=(8, 6))
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, palette="Set1")

# Show the plot
plt.title('Categorical Scatterplot with Jitter')
plt.show()
