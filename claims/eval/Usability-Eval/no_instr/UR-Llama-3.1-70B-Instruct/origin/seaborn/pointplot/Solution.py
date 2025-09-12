# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Define a figure and axis
fig, ax = plt.subplots()

# Show point estimates and errors using lines with markers
sns.lineplot(data=tips, x="sex", y="total_bill", marker="o", err_style="bars", ax=ax)

# Set plot title
ax.set_title("Point Estimates and Errors")

# Show the plot
plt.show()
