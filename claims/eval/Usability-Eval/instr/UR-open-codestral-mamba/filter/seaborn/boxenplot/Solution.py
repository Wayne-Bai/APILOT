import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Assume that 'data' is the pandas DataFrame.
# 'column' is the column from the DataFrame that you want to plot as boxplot.
data = sns.load_dataset('iris')
column = 'sepal_length'

plt.figure(figsize=(10,8))
sns.boxplot(x=data[column], palette = "Set3")
plt.title('Enhanced Boxplot')
plt.show()
