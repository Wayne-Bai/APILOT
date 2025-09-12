# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Create a categorical scatterplot
sns.swarmplot(data=tips, x="day", y="total_bill", hue="sex")

# Set title and labels
plt.title("Categorical Scatterplot")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill")

# Show the plot
plt.show()
