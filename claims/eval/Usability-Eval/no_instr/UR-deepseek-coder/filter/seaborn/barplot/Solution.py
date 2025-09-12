import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Mean': [2.3, 3.1, 1.7, 2.8],
    'Lower_error': [0.2, 0.3, 0.1, 0.2],
    'Upper_error': [0.3, 0.4, 0.2, 0.3]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(8, 6))
sns.barplot(x='Category', y='Mean', yerr=[df['Lower_error'], df['Upper_error']], capsize=0.2, data=df)
plt.title('Point Estimates and Errors as Rectangular Bars')
plt.ylabel('Mean Value')
plt.xlabel('Category')
plt.show()
