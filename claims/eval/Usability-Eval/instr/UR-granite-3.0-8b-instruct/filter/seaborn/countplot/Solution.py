import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame and 'column_name' is your categorical column
sns.countplot(x='column_name', data=df)
plt.show()
