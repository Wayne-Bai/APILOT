import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame 'df' with a categorical column 'category'
# Replace 'category' with your actual column name

# Count the occurrences of each category
category_counts = df['category'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=category_counts.index, y=category_counts.values)
plt.title('Counts of Observations in Each Categorical Bin')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()
