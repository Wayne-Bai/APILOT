import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Mean': [2.5, 3.7, 1.8, 4.2],
    'Lower_error': [0.2, 0.3, 0.1, 0.4],
    'Upper_error': [0.3, 0.4, 0.2, 0.5]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate the error range
df['Error'] = list(zip(df['Lower_error'], df['Upper_error']))

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Mean', yerr=df['Error'].tolist(), data=df, capsize=.2)

plt.title('Point Estimates and Errors as Rectangular Bars')
plt.xlabel('Category')
plt.ylabel('Mean Value')
plt.show()
