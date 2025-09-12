import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = {'Group': ['A', 'B', 'C', 'D', 'E'],
        'Point Estimate': [10, 15, 20, 25, 30],
        'Lower Error': [8, 12, 16, 20, 24],
        'Upper Error': [12, 18, 24, 30, 36]}

# Create DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Group', y='Point Estimate', data=df, color='blue', label='Point Estimate')
sns.barplot(x='Group', y='Lower Error', data=df, color='lightblue', label='Lower Error', bottom='Point Estimate')
sns.barplot(x='Group', y='Upper Error', data=df, color='lightcoral', label='Upper Error', bottom='Point Estimate')

plt.title('Point Estimates and Errors as Rectangular Bars')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.legend()
plt.show()
