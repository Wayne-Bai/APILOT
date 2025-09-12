import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# apply theme/style seaborn
sns.set_style('whitegrid')

# Create some random data for the illustration
data = {
    "Group": ['A', 'A', 'A', 'B', 'B', 'B'],
    "Observation1": [11.0, 12.0, 14.0, 18.0, 17.0, 16.0],
    "Observation2": [16.0, 14.0, 15.0, 11.0, 13.0, 14.0]
}
df = pd.DataFrame(data)

# Create the point and error bar plot
plt.figure(figsize=(10, 6))

sns.barplot(x='Group', y='Observation1', data=df, ci='sd', capsize=0.2)

# add title and labels
plt.title('Point Estimates and Errors')
plt.ylabel('Observation Value')
plt.xlabel('Group')

plt.show()
