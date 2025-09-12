import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame and 'variable' is the column containing the data
sns.set_style("whitegrid")
ax = sns.boxplot(x=df['variable'])

# Add point estimates (mean) and errors (standard deviation) as rectangular bars
for box in ax.boxes:
    mean = box.get_ydata()[0]
    std = box.get_ydata()[1]
    ax.text(box.get_x() + box.get_width()/2, mean + std, f'Mean: {mean:.2f}, SD: {std:.2f}', ha='center', fontsize=8)

plt.show()
