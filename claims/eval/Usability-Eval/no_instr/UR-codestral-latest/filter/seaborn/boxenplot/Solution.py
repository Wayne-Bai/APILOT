import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame df and the column 'data_column' contains the data.
sns.boxplot(data=df, x='data_column')
plt.title('Enhanced Box Plot of the Data')
plt.show()
