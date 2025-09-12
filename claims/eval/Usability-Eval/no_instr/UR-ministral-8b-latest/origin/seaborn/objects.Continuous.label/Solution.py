import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data for Demo
tips = sns.load_dataset("tips")

# Create a basic plot
plt.figure(figsize=(8, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")

# Rotate x-axis labels
plt.xticks(rotation=45)

# Customize tick labels in the legend
handles = plt.gca().get_legend_handles_labels()[0]
labels = plt.gca().get_legend_handles_labels()[1]
for i, label in enumerate(labels):
    if label == 'Female':
        labels[i] = 'Females'
    elif label == 'Male':
        labels[i] = 'Males'

plt.legend(handle=handles, labels=labels, title='Gender')

plt.show()
