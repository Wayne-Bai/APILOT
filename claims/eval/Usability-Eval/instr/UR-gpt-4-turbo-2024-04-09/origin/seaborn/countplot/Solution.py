import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = sns.load_dataset('titanic')

# Create a countplot using seaborn's barplot function by counting instances
sns.barplot(x="class", y=None, data=data, estimator=lambda x: len(x), ci=None)

# Add labels and title
plt.ylabel('Count')
plt.title('Counts of Observations in Each Class')
plt.show()
