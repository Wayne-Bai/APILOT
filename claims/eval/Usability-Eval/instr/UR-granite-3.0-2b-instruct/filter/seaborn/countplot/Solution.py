import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame and 'category' is the column with categorical data
sns.countplot(x='category', data=df)
plt.show()
