import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Estimate': [10, 15, 12, 13, 17],
    'Lower CI': [8, 10, 10, 11, 13],
    'Upper CI': [11, 18, 15, 15, 19]
}

# Convert data to DataFrame
df = sns.util._pandas_tools.df(data)

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Estimate', y='Lower CI', color='blue', label='Estimate')
sns.barplot(data=df, x='Estimate', y='Upper CI', color='red', label='Errors')

# Adding labels and title
plt.xlabel('Estimate')
plt.ylabel('Values')
plt.title('Point Estimates and Errors as Rectangular Bars')

# Display the plot
plt.legend()
plt.show()
