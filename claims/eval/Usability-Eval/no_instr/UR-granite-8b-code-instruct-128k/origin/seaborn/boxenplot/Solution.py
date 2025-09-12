import seaborn as sns

# Load your dataset into a pandas DataFrame
data = pd.read_csv('your_data.csv')

# Select the columns you want to plot
cols = ['column1', 'column2', 'column3']

# Create the box plot
sns.boxplot(data=data[cols])

# Add labels and titles
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.title('title')

# Show the plot
plt.show()
