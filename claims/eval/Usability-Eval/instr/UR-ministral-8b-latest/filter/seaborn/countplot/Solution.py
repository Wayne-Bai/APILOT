import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']
}

df = pd.DataFrame(data)

# Plot the counts of observations in each categorical bin using bars
sns.countplot(x='category', data=df)
plt.title('Counts of Observations in Each Categorical Bin')
plt.show()
