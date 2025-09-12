import seaborn as sns
import matplotlib.pyplot as plt

# Create a simulation dataset
sns.set(style="ticks")
data = sns.load_dataset("tips")

# Draw a KDE plot
plt.figure(figsize=(10, 6))
sns.kdeplot(data[data.category == "Lunch"].total_bill, color="blue", label="Lunch")
sns.kdeplot(data[data.category == "Dinner"].total_bill, color="green", label="Dinner")

# Add box plot overlay
sns.boxplot(x="category", y="total_bill", data=data)

plt.title("KDE Plot with Overlay Box Plot")
plt.xlabel("Category")
plt.ylabel("Total Bill")
plt.legend()
plt.show()
