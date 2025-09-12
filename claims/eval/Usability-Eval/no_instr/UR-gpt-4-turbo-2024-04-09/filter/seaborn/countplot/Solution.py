import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset('titanic')

# Create a count plot
sns.countplot(x='class', data=data)

plt.title('Counts of Observations for Each Class')
plt.show()
