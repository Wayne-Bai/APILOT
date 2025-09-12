import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
df = sns.load_dataset('tips')

# Point estimates and errors with summary stats
df_means = df.melt().dropna().groupby('variable').mean().reset_index()

# Plot means and errors with standard error as the error
plt.figure(figsize=(10, 6))
sns.lineplot(x='index', y='value', yerr=df_means['value'] * 1.96 / df_means['index'].shape[0], data=df_means, marker='o')

# Labels and title
plt.xlabel('Index')
plt.ylabel('Mean Value')
plt.title('Point Estimates and Errors with Standard Error as Margin of Error')

# Display the plot
plt.show()
