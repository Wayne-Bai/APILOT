import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Assume that 'df' is your DataFrame and 'column_name' is the name of your categorical column
sns.countplot(x='column_name', data=df)
plt.show()
