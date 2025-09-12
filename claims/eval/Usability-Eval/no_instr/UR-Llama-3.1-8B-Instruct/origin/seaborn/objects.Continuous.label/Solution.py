# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the example tips dataset
tips = sns.load_dataset("tips")

# Create a scatter plot
plt.figure(figsize=(8,6))
plt.scatter(tips['total_bill'], tips['tip'])

# Set the title and labels
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')

# Configure the appearance of tick labels for the scale’s axis or legend
# To change the font size of the scale's axis ticks
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# To rotate the tick labels for readability
plt.xticks(rotation=45)
plt.yticks(rotation=0)

# To change the font style of the scale's axis ticks
plt.xticks(fontstyle='italic')
plt.yticks(fontstyle='italic')

# To change the color of the scale's axis ticks
plt.xticks(color='red')
plt.yticks(color='blue')

# Show the plot
plt.show()
