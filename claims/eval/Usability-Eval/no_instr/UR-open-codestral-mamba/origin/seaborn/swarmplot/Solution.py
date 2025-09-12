import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Some data
data = sns.load_dataset("tips")

# Create a numerical representation of the categorical variable
using_encoding = {category: k for k, category in enumerate(data['sex'].unique())}
data['sex_encoding'] = [using_encoding[x] for x in data['sex']]

# Add jitter on 'sex_encoding'
data['sex_encoding'] = data['sex_encoding'] + np.random.randn(len(data)) * 0.05

# Creating a categorical scatterplot with point adjustments
plt.figure(figsize=(8,6))
sns.stripplot(x="total_bill", y="sex_encoding", hue="smoker", data=data, size=4, jitter=False)
plt.title('Scatter plot with adjusted points')
plt.show()
