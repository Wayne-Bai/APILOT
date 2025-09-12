import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a figure and axis
fig, ax = plt.subplots()

# Draw a KDE plot
sns.kdeplot(data=tips, x="total_bill", ax=ax)

# Add box plot statistics
sns.boxplot(data=tips, x="total_bill", ax=ax, width=0.1, color="white")

# Show the plot
plt.show()
