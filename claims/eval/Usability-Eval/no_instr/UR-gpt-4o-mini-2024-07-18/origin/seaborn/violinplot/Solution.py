import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
data = sns.load_dataset("tips")

# Create a figure and set of subplots
plt.figure(figsize=(10, 6))

# Draw a KDE plot
sns.kdeplot(data=data, x="total_bill", fill=True, alpha=0.3)

# Overlay a box plot
sns.boxplot(data=data, x="total_bill", color="red", width=0.3, fliersize=0)

# Display the plot
plt.title("KDE and Box Plot of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Density")
plt.show()
