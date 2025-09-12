import seaborn as sns
import matplotlib.pyplot as plt

# Assuming we have a DataFrame df with categorical column 'category'
df = sns.load_dataset('titanic')

# Display counts of observations in each categorical bin
plt.figure(figsize=(8, 6))
sns.countplot(x='class', data=df, palette='muted')
plt.title('Counts of Observations in Each Categorical Bin')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()
