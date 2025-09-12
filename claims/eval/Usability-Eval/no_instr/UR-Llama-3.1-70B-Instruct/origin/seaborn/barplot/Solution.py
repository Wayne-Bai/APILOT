# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset("tips")

# Define categories
xfmt = ['Female', 'Male']
x = [0, 1]
y = [19.79138847, 23.34375]

# Calculate the standard error
yerr = [[0.33891564, 0.67872536], [0.72582869, 1.49771593]]

# Create a new figure
plt.figure(figsize=(10,6))

# Use seaborn styling
sns.set_style("whitegrid")

# Plot the bar chart with error bars
sns.barplot(xfmt, y, yerr=sum(yerr, []))

# Set labels and title
plt.xlabel('Sex')
plt.ylabel('Total Bill')
plt.title('Total Bill vs Sex of Customers')

# Show the plot
plt.show()
