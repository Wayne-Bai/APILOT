import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a sample dataset
np.random.seed(10)
data = {
    'Category': ['A', 'B', 'C', 'D']*10,
    'Value': np.random.normal(loc=0, scale=1, size=40)
}

df = pd.DataFrame(data)

# Calculate the point estimates (mean) and confidence intervals
point_estimates = df.groupby('Category')['Value'].mean().reset_index()
confidence_intervals = df.groupby('Category')['Value'].sem().reset_index()

# Plot using seaborn's barplot to show point estimates and errors as rectangular bars
plt.figure(figsize=(8, 6))
sns.barplot(x='Category', y='Value', data=point_estimates, capsize=.2, ci=None)

# Add error bars manually
for index, row in point_estimates.iterrows():
    plt.errorbar(
        row['Category'],
        row['Value'],
        yerr=confidence_intervals.loc[index, 'Value'],
        fmt='none',
        c='black',
        capsize=5
    )

plt.title("Point Estimates and Errors as Rectangular Bars")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()
