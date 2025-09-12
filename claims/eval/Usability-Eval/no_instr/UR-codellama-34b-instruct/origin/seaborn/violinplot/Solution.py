import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data.csv')

# Create a figure with a single axis
fig, ax = plt.subplots(1)

# Draw the KDE plot
sns.kdeplot(data=data, shade=True, cmap='Blues', ax=ax)

# Add observations or box plot statistics
sns.add_statistics(data, kind='box')

# Customize the appearance of the plot
sns.set_style('whitegrid')
plt.title('Kernel Density Estimate and Box Plot Statistics')
plt.xlabel('Variable')
plt.ylabel('Density')

# Show the plot
plt.show()
