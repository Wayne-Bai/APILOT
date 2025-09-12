import seaborn as sns
import matplotlib.pyplot as plt

# Assuming we have a dataframe called 'df' and a categorical column called 'category'

# use countplot
sns.countplot(x='category', data=df)

# Show the plot
plt.show()
