import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame called 'df' with a categorical column 'category'
sns.countplot(x='category', data=df)
plt.show()
