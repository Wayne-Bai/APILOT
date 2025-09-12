import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {'Measurement_A': [3.2, 4.0, 5.1, 6.5, 8.3],
        'Measurement_B': [7.0, 6.5, 7.2, 8.1, 6.8],
        'Measurement_C': [3.4, 1.9, 2.1, 3.3, 1.1]}

df = pd.DataFrame(data)

# Scatter plot with errors
sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.lmplot(x='Measurement_A', y='Measurement_B', data=df,
           regplot=True, aspect=1.5, height=6, markers="o", markeredgecolor="black", markeredgewidth=1.5, _c='k')

plt.title('Scatter plot with Point Estimates and Errors')
plt.xlabel('Measurement A')
plt.ylabel('Measurement B')
plt.show()
