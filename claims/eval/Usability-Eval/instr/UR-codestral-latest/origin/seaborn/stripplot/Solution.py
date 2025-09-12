import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'df' is your DataFrame and 'category' is the column that holds categories
sns.stripplot(x="category", y="value", data=df, jitter=True)
plt.show()
