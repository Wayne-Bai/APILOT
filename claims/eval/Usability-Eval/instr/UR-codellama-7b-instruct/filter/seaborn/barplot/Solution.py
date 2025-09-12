
import seaborn as sns
import matplotlib.pyplot as plt

# Set the data for the bar chart
data = {'Point Estimate': [10, 20, 30], 'Lower Error Bound': [9, 18, 27], 'Upper Error Bound': [11, 22, 33]}

# Plot the bar chart with error bars
sns.barplot(x='Point Estimate', y=data['Upper Error Bound'], data=data)
plt.ylabel('Error Bar')
plt.xlabel('Point Estimate')
plt.title('Bar Chart with Error Bars')

# Add error bars
plt.errorbar(x=data['Point Estimate'], y=data['Upper Error Bound'], xerr=data['Lower Error Bound'] - data['Point Estimate'])

# Show the plot
plt.show()
