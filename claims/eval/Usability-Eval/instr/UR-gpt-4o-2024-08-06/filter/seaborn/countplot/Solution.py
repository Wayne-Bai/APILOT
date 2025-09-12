import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'B', 'C', 'C', 'C'],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting barplot to show counts of observations in each categorical bin
sns.barplot(x=df['category'].value_counts().index, y=df['category'].value_counts().values)

# Adding labels and title
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Counts of Observations in Each Categorical Bin')
plt.show()
