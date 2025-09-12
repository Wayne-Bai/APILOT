# Importing necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Loading the tips dataset
tips = sns.load_dataset("tips")

# Create a figure and axis
fig, ax = plt.subplots()

# Show point estimates and errors as rectangular bars
sns.barplot(data=tips, x="day", y="total_bill", ci="sd", capsize=0.2, ax=ax)

# Set labels and title
ax.set_title("Total Bill by Day of the Week")
ax.set_xlabel("Day of the Week")
ax.set_ylabel("Total Bill ($USD)")

# Show the plot
plt.show()
