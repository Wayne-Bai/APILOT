# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the example tips dataset
tips = sns.load_dataset('tips')

# Crossover plot
plt.figure(figsize=(8,6))
sns.cplot(x='day', y='total_bill', kind='point', data=tips, 
          errorbar='ci', estimator=None, color='royalblue', palette='husl',
          hue='sex', markers=['o','s'], clip=[0, tips['total_bill'].max()])

# Set the title and labels
plt.title('Relationship between Total Bill and Day of the Week')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.xticks(['Thur', 'Fri', 'Sat', 'Sun'])

# Show the plot
plt.show()
