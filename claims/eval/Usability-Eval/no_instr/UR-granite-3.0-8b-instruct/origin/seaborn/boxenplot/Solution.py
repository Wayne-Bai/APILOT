import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame df with columns 'category' and 'value'
sns.boxplot(x='category', y='value', data=df)
plt.show()
