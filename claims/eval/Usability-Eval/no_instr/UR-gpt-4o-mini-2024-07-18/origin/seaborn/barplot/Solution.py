import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Point Estimate': [10, 15, 7, 12],
    'Error': [2, 3, 1, 2]
}

df = pd.DataFrame(data)

# Create the plot
plt.figure(figsize=(8, 5))
sns.barplot(x='Category', y='Point Estimate', data=df, ci=None)

# Add error bars
for index, row in df.iterrows():
    plt.errorbar(x=row['Category'], 
                 y=row['Point Estimate'], 
                 yerr=row['Error'], 
                 fmt='none', 
                 c='black', 
                 capsize=5)

plt.title('Point Estimates with Error Bars')
plt.xlabel('Category')
plt.ylabel('Point Estimate')
plt.show()
