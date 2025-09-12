import seaborn as sns
import matplotlib.pyplot as plt

# Load an example dataset
flights = sns.load_dataset('flights')

# Create line plot with point markers
plt.figure(figsize=(10,6))
plot = sns.lineplot(data=flights, x='year', y='passengers', marker='o', err_style='bars', ci=68, color='b')
plt.title('Line plot with point markers representing point estimates and errors')
plt.show()
